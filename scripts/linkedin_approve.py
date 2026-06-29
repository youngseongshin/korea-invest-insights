#!/usr/bin/env python3
"""Review and approve staged LinkedIn posts (semi-automatic publishing).

The distribution pipeline STAGES each new post into a pending queue instead of
auto-posting. Run this to review the composed text and approve posting to your
personal LinkedIn profile.

    scripts/linkedin_approve.py             # interactively review all pending
    scripts/linkedin_approve.py --list      # just list pending
    scripts/linkedin_approve.py --slug X    # approve + post one slug
    scripts/linkedin_approve.py --all       # review each pending entry

Pending queue: ~/.local/share/korea-invest-insights/linkedin_pending.json
Token/secrets: ~/.config/korea-invest-insights/linkedin.env (linkedin_oauth_setup.py)
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
from pathlib import Path

from linkedin_notify import (  # same scripts/ dir
    build_commentary,
    post_to_linkedin,
    read_env,
    refresh_access_token,
)

DATA_DIR = Path.home() / ".local" / "share" / "korea-invest-insights"
PENDING_PATH = DATA_DIR / "linkedin_pending.json"
LOG_PATH = DATA_DIR / "linkedin_distribution_log.json"
AUTO_APPROVE_ENV = "KII_LINKEDIN_ALLOW_AUTO_APPROVE"


def _load(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _save(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _record_distributed(url: str, slug: str) -> None:
    log = _load(LOG_PATH)
    log.setdefault("posts", {})
    log["posts"][url] = {
        "mode": "publish",
        "at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "response": {"slug": slug, "url": url},
    }
    _save(LOG_PATH, log)


def _remove_pending(url: str) -> None:
    data = _load(PENDING_PATH)
    if data.get("pending", {}).pop(url, None) is not None:
        _save(PENDING_PATH, data)


def _publish(entry: dict, env: dict) -> bool:
    token = env.get("LINKEDIN_ACCESS_TOKEN")
    urn = env.get("LINKEDIN_MEMBER_URN")
    if not token or not urn:
        print("토큰이 없습니다. 먼저 scripts/linkedin_oauth_setup.py 를 실행하세요.")
        return False
    commentary = build_commentary(entry["title"], entry.get("desc", ""), entry["url"])
    ok, detail = post_to_linkedin(token, urn, commentary)
    if not ok and detail.startswith("HTTP 401"):
        refreshed = refresh_access_token(env)
        if refreshed:
            ok, detail = post_to_linkedin(refreshed, urn, commentary)
    if ok:
        print(f"✅ LinkedIn 게시 완료 — {entry['url']}  (postId {detail})")
        _record_distributed(entry["url"], entry["slug"])
        _remove_pending(entry["url"])
    else:
        print(f"❌ 게시 실패 — {detail}")
    return ok


def _preview(entry: dict) -> None:
    env_desc = entry.get("desc", "")
    commentary = build_commentary(entry["title"], env_desc, entry["url"])
    print("\n" + "=" * 72)
    print(f"slug : {entry['slug']}")
    print(f"staged: {entry.get('staged_at', '')}")
    print("-" * 72)
    print(commentary)
    print("=" * 72)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Approve and post staged LinkedIn entries.")
    parser.add_argument("--list", action="store_true", help="list pending posts and exit")
    parser.add_argument("--slug", default="", help="approve + post a single slug")
    parser.add_argument("--all", action="store_true", help="post all pending")
    parser.add_argument(
        "--yes",
        action="store_true",
        help=f"skip the y/N prompt only when {AUTO_APPROVE_ENV}=1 is set",
    )
    args = parser.parse_args(argv)

    if args.yes and os.environ.get(AUTO_APPROVE_ENV) != "1":
        print(
            "LinkedIn 자동 승인은 비활성화되어 있습니다. "
            f"정말 필요한 1회성 수동 예외에서만 {AUTO_APPROVE_ENV}=1 을 설정하세요."
        )
        return 2

    data = _load(PENDING_PATH)
    pending = list(data.get("pending", {}).values())
    pending.sort(key=lambda e: e.get("staged_at", ""))

    if not pending:
        print("승인 대기 중인 LinkedIn 게시물이 없습니다.")
        return 0

    if args.list:
        print(f"승인 대기 {len(pending)}건:")
        for e in pending:
            print(f"  - {e['slug']}  ({e['url']})")
        return 0

    env = read_env()

    targets = pending
    if args.slug:
        targets = [e for e in pending if e["slug"] == args.slug]
        if not targets:
            print(f"대기 큐에 slug={args.slug!r} 가 없습니다.")
            return 1

    posted = 0
    for entry in targets:
        _preview(entry)
        if args.yes or args.all and args.yes:
            approve = True
        elif args.all:
            ans = input("이 글을 게시할까요? [y/N/q(종료)] ").strip().lower()
            if ans == "q":
                break
            approve = ans == "y"
        else:
            ans = input("이 글을 게시할까요? [y/N/q(종료)] ").strip().lower()
            if ans == "q":
                break
            approve = ans == "y"
        if approve:
            if _publish(entry, env):
                posted += 1
        else:
            print("건너뜀.")

    print(f"\n완료: {posted}건 게시.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
