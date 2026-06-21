#!/usr/bin/env python3
"""Publish a blog post to a personal LinkedIn profile via the LinkedIn Posts API.

This is the worker invoked by ``post_publish_distribution.py`` for the
``linkedin`` channel. It is intentionally stdlib-only (urllib) to match the rest
of the distribution tooling.

Secrets are read at runtime from a LOCAL env file (never committed):

    ~/.config/korea-invest-insights/linkedin.env

Required keys (created by ``scripts/linkedin_oauth_setup.py``):
    LINKEDIN_ACCESS_TOKEN   - member access token with w_member_social scope
    LINKEDIN_MEMBER_URN     - urn:li:person:<sub>

Optional keys (enable silent auto-refresh when the access token has expired):
    LINKEDIN_REFRESH_TOKEN
    LINKEDIN_CLIENT_ID
    LINKEDIN_CLIENT_SECRET
    LINKEDIN_TOKEN_EXPIRES_AT   - unix seconds

Exit codes:
    0  posted (prints JSON {"status": "published", ...})
    2  not configured / no valid token (prints {"status": "no_token", ...})
    1  hard API failure (prints {"status": "error", ...})

The distribution wrapper treats a non-zero LinkedIn exit as a NON-fatal skip so
a missing/expired token never blocks the other channels.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ENV_PATH = Path.home() / ".config" / "korea-invest-insights" / "linkedin.env"
POSTS_URL = "https://api.linkedin.com/rest/posts"
TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"
# LinkedIn requires a dated version header (YYYYMM). Bump as needed.
LINKEDIN_VERSION = "202401"


def read_env(path: Path = ENV_PATH) -> dict[str, str]:
    env: dict[str, str] = {}
    if not path.exists():
        return env
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def write_env(env: dict[str, str], path: Path = ENV_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"{k}={v}" for k, v in env.items()]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    try:
        path.chmod(0o600)
    except OSError:
        pass


def refresh_access_token(env: dict[str, str]) -> str | None:
    """Try to refresh the access token. Returns the new token or None."""
    refresh = env.get("LINKEDIN_REFRESH_TOKEN")
    client_id = env.get("LINKEDIN_CLIENT_ID")
    client_secret = env.get("LINKEDIN_CLIENT_SECRET")
    if not (refresh and client_id and client_secret):
        return None
    data = urllib.parse.urlencode(
        {
            "grant_type": "refresh_token",
            "refresh_token": refresh,
            "client_id": client_id,
            "client_secret": client_secret,
        }
    ).encode("utf-8")
    req = urllib.request.Request(TOKEN_URL, data=data, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, json.JSONDecodeError):
        return None
    token = payload.get("access_token")
    if not token:
        return None
    env["LINKEDIN_ACCESS_TOKEN"] = token
    if payload.get("refresh_token"):
        env["LINKEDIN_REFRESH_TOKEN"] = payload["refresh_token"]
    if payload.get("expires_in"):
        env["LINKEDIN_TOKEN_EXPIRES_AT"] = str(int(time.time()) + int(payload["expires_in"]))
    write_env(env)
    return token


def build_commentary(title: str, description: str, url: str) -> str:
    parts = [title.strip()]
    desc = (description or "").strip()
    if desc:
        # Keep the teaser short; LinkedIn renders a link card from the URL.
        parts.append(desc if len(desc) <= 600 else desc[:597] + "...")
    parts.append(url.strip())
    return "\n\n".join(p for p in parts if p)


def post_to_linkedin(token: str, member_urn: str, commentary: str) -> tuple[bool, str]:
    body = {
        "author": member_urn,
        "commentary": commentary,
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": [],
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False,
    }
    req = urllib.request.Request(POSTS_URL, data=json.dumps(body).encode("utf-8"), method="POST")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", "application/json")
    req.add_header("X-Restli-Protocol-Version", "2.0.0")
    req.add_header("LinkedIn-Version", LINKEDIN_VERSION)
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            post_id = resp.headers.get("x-restli-id") or resp.headers.get("X-RestLi-Id") or ""
            return True, post_id
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "ignore")[:400]
        return False, f"HTTP {exc.code}: {detail}"
    except urllib.error.URLError as exc:
        return False, f"network error: {exc}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Post a blog entry to a personal LinkedIn profile.")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--desc", default="")
    args = parser.parse_args(argv)

    env = read_env()
    token = env.get("LINKEDIN_ACCESS_TOKEN")
    member_urn = env.get("LINKEDIN_MEMBER_URN")
    if not token or not member_urn:
        print(json.dumps({"status": "no_token", "slug": args.slug,
                          "reason": f"LinkedIn not configured. Run scripts/linkedin_oauth_setup.py ({ENV_PATH})"},
                         ensure_ascii=False))
        return 2

    # Proactive refresh if we know the token is expired.
    expires_at = env.get("LINKEDIN_TOKEN_EXPIRES_AT")
    if expires_at and expires_at.isdigit() and int(expires_at) <= int(time.time()):
        refreshed = refresh_access_token(env)
        if refreshed:
            token = refreshed

    commentary = build_commentary(args.title, args.desc, args.url)
    ok, detail = post_to_linkedin(token, member_urn, commentary)

    # One retry after a refresh on an auth failure (token may have expired early).
    if not ok and detail.startswith("HTTP 401"):
        refreshed = refresh_access_token(env)
        if refreshed:
            ok, detail = post_to_linkedin(refreshed, member_urn, commentary)

    if ok:
        print(json.dumps({"status": "published", "slug": args.slug, "url": args.url,
                          "postId": detail}, ensure_ascii=False))
        return 0
    print(json.dumps({"status": "error", "slug": args.slug, "url": args.url,
                      "detail": detail}, ensure_ascii=False))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
