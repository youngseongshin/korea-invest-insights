#!/usr/bin/env python3
"""Local Valley auto-publisher for newly live Korea Invest Insights posts.

This is intentionally a local-only poller. Valley currently relies on a
session-backed web API, so credentials should live on the user's Mac rather
than in GitHub Actions or the repository.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

import valley_crosspost as valley


DEFAULT_CONFIG_PATH = Path.home() / ".config" / "korea-invest-insights" / "valley.env"
DEFAULT_REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LANG = "ko"
DEFAULT_STATE_PATH = (
    Path.home()
    / ".local"
    / "share"
    / "korea-invest-insights"
    / "valley_auto_publish_state.json"
)


def load_env_file(path: Path) -> bool:
    """Load KEY=VALUE pairs without echoing secrets."""
    path = path.expanduser()
    if not path.exists():
        return False

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value
    return True


def truthy(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "y", "on"}


def read_crosspost_log(path: Path) -> dict[str, Any]:
    try:
        return valley.load_log(path.expanduser())
    except (json.JSONDecodeError, OSError):
        return {"posts": {}}


def load_state(path: Path) -> dict[str, Any]:
    path = path.expanduser()
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def save_state(path: Path, state: dict[str, Any]) -> None:
    path = path.expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_iso_timestamp(value: Any) -> float | None:
    if not value:
        return None
    try:
        parsed = dt.datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.timestamp()


def is_recent(post: dict[str, Any], path: Path, since_days: int) -> bool:
    if since_days <= 0:
        return True
    parsed = valley.parse_date(post.get("date"))
    timestamp = valley.date_sort_key(parsed, path.stat().st_mtime)
    cutoff = dt.datetime.now(dt.timezone.utc).timestamp() - since_days * 86400
    return timestamp >= cutoff


def is_live(url: str, timeout: int = 12) -> tuple[bool, str]:
    request = urllib.request.Request(url, method="GET")
    request.add_header("User-Agent", "korea-invest-insights-valley-auto-publish/0.1")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return 200 <= response.status < 400, f"HTTP {response.status}"
    except urllib.error.HTTPError as error:
        return False, f"HTTP {error.code}"
    except urllib.error.URLError as error:
        return False, str(error.reason)
    except TimeoutError:
        return False, "timeout"


def discover_candidates(
    repo_root: Path,
    lang: str,
    since_days: int,
    log_path: Path,
    min_timestamp: float | None,
) -> list[dict[str, Any]]:
    post_paths = sorted((repo_root / "content" / "post").glob(f"*/index.{lang}.md"))
    log = read_crosspost_log(log_path)
    sent_urls = set(log.get("posts", {}).keys())
    candidates: list[tuple[float, dict[str, Any]]] = []

    for path in post_paths:
        post = valley.load_post(path)
        if post["front_matter"].get("draft") is True:
            continue
        if post["canonical_url"] in sent_urls:
            continue
        if not is_recent(post, path, since_days):
            continue
        parsed = valley.parse_date(post.get("date"))
        sort_key = valley.date_sort_key(parsed, path.stat().st_mtime)
        if min_timestamp is not None and sort_key < min_timestamp:
            continue
        candidates.append((sort_key, post))

    # Publish older pending live posts first so Valley follows the site order.
    candidates.sort(key=lambda item: item[0])
    return [post for _, post in candidates]


def credential_state() -> tuple[bool, str]:
    if os.environ.get("VALLEY_API_TOKEN", "").strip():
        return True, "token"
    if os.environ.get("VALLEY_COOKIE", "").strip():
        return True, "cookie"
    return False, "missing"


def publish_post(post: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    payload = valley.build_valley_payload(post, args.body_mode, args.category_id)
    response = valley.api_request(
        "POST",
        "/post/posts",
        {"post": payload},
        args.api_base.rstrip("/"),
    )
    summary = valley.summarize_response(response)
    valley.record_crosspost(Path(args.log_path).expanduser(), post["canonical_url"], "publish", summary)
    return summary


def run(args: argparse.Namespace) -> int:
    config_loaded = load_env_file(Path(args.config))
    args.category_id = args.category_id or os.environ.get("VALLEY_POST_CATEGORY_ID")
    args.api_base = args.api_base or os.environ.get("VALLEY_API_BASE", valley.VALLEY_API_BASE_URL)

    if not args.dry_run and not truthy(os.environ.get("VALLEY_AUTO_PUBLISH")):
        print(
            json.dumps(
                {
                    "status": "skipped",
                    "reason": "VALLEY_AUTO_PUBLISH is not true",
                    "configLoaded": config_loaded,
                },
                ensure_ascii=False,
            )
        )
        return 0

    has_credentials, credential_kind = credential_state()
    if not args.dry_run:
        if not has_credentials:
            print(
                json.dumps(
                    {
                        "status": "skipped",
                        "reason": "Valley credentials missing",
                        "configLoaded": config_loaded,
                        "configPath": str(Path(args.config).expanduser()),
                    },
                    ensure_ascii=False,
                )
            )
            return 0
        if not args.category_id:
            print(
                json.dumps(
                    {
                        "status": "skipped",
                        "reason": "VALLEY_POST_CATEGORY_ID missing",
                        "credentialKind": credential_kind,
                    },
                    ensure_ascii=False,
                )
            )
            return 0

    repo_root = Path(args.repo_root).resolve()
    log_path = Path(args.log_path).expanduser()
    state_path = Path(args.state_path).expanduser()
    state = load_state(state_path)
    state_started_at = parse_iso_timestamp(os.environ.get("VALLEY_AUTO_PUBLISH_START_AT")) or parse_iso_timestamp(
        state.get("startedAt")
    )

    if not args.dry_run and state_started_at is None and not args.allow_backfill and not truthy(os.environ.get("VALLEY_BACKFILL")):
        now = dt.datetime.now(dt.timezone.utc).isoformat()
        save_state(state_path, {"startedAt": now, "backfill": False})
        print(
            json.dumps(
                {
                    "status": "initialized",
                    "reason": "Created first-run watermark; existing posts were not backfilled",
                    "statePath": str(state_path),
                    "startedAt": now,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    candidates = discover_candidates(repo_root, args.lang, args.since_days, log_path, state_started_at)

    results: list[dict[str, Any]] = []
    published = 0
    for post in candidates:
        if published >= args.max_posts:
            break

        live_ok = True
        live_detail = "not checked"
        if args.require_live:
            live_ok, live_detail = is_live(post["canonical_url"])
        if not live_ok:
            results.append(
                {
                    "status": "pending_live",
                    "title": post["title"],
                    "url": post["canonical_url"],
                    "live": live_detail,
                }
            )
            continue

        if args.dry_run:
            results.append(
                {
                    "status": "would_publish",
                    "title": post["title"],
                    "url": post["canonical_url"],
                    "live": live_detail,
                }
            )
            published += 1
            continue

        try:
            valley_summary = publish_post(post, args)
        except valley.ValleyCrosspostError as error:
            results.append(
                {
                    "status": "error",
                    "title": post["title"],
                    "url": post["canonical_url"],
                    "error": str(error),
                }
            )
            print(json.dumps({"status": "failed", "results": results}, ensure_ascii=False, indent=2))
            return 1

        published += 1
        results.append(
            {
                "status": "published",
                "title": post["title"],
                "url": post["canonical_url"],
                "valley": valley_summary,
            }
        )

    print(
        json.dumps(
            {
                "status": "ok",
                "dryRun": args.dry_run,
                "configLoaded": config_loaded,
                "credentialKind": credential_kind if has_credentials else None,
                "startedAt": state.get("startedAt") or os.environ.get("VALLEY_AUTO_PUBLISH_START_AT"),
                "candidateCount": len(candidates),
                "processedCount": len(results),
                "results": results,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Publish newly live local Hugo posts to Valley.")
    parser.add_argument("--repo-root", default=str(DEFAULT_REPO_ROOT))
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH))
    parser.add_argument("--lang", default=DEFAULT_LANG)
    parser.add_argument("--since-days", type=int, default=14)
    parser.add_argument("--max-posts", type=int, default=3)
    parser.add_argument("--body-mode", choices=("auto", "teaser", "full"), default="auto")
    parser.add_argument("--category-id", default=os.environ.get("VALLEY_POST_CATEGORY_ID"))
    parser.add_argument("--api-base", default=os.environ.get("VALLEY_API_BASE", valley.VALLEY_API_BASE_URL))
    parser.add_argument("--log-path", default=str(valley.DEFAULT_LOG_PATH))
    parser.add_argument("--state-path", default=str(DEFAULT_STATE_PATH))
    parser.add_argument("--require-live", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--allow-backfill", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main() -> int:
    try:
        return run(build_parser().parse_args())
    except Exception as error:  # Defensive launchd boundary.
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
