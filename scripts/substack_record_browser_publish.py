#!/usr/bin/env python3
"""Record a Substack post published from the built-in browser.

The browser path (scripts/substack_pane_push.js in a logged-in pane) is the standard
Substack route since 2026-10-23. This script writes its receipt into the Substack
distribution log under the same key post_publish_distribution.py reads, so the
Substack-first gate passes and the other channels can run.

  --check            print the receipt for --slug and exit 0, or exit 1 when there is none
  default            verify the public Substack URL answers 200, then write the receipt

The Note is part of the standard. Pass --no-note "<reason>" only for an explicit
exception; the reason is stored in the receipt.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

import post_publish_distribution as ppd
import valley_crosspost as valley

SUBSTACK_URL_RE = re.compile(r"^https://[a-z0-9-]+\.substack\.com/p/[A-Za-z0-9-]+/?$")
NOTE_URL_RE = re.compile(r"^https://substack\.com/(@[A-Za-z0-9_-]+/)?note/c-\d+/?$")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


def receipt_key(repo_root: Path, slug: str, lang: str) -> str:
    post_path = repo_root / "content" / "post" / slug / f"index.{lang}.md"
    if not post_path.exists():
        raise SystemExit(f"post not found: {post_path}")
    return valley.load_post(post_path)["canonical_url"]


def public_status(url: str) -> int:
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return e.code
    except OSError:
        return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--slug", required=True)
    parser.add_argument("--repo-root", default=str(ppd.DEFAULT_REPO_ROOT))
    parser.add_argument("--lang", default="ko", help="key language; must match post_publish_distribution --lang")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--substack-url", default="")
    parser.add_argument("--draft-id", type=int, default=0)
    parser.add_argument("--note-url", default="")
    parser.add_argument("--no-note", default="", metavar="REASON")
    parser.add_argument("--emailed", choices=("yes", "no"), default="yes",
                        help="whether the publish call used send:true")
    parser.add_argument("--no-live-check", action="store_true")
    parser.add_argument("--force", action="store_true", help="replace an existing receipt")
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    key = receipt_key(repo_root, args.slug, args.lang)
    log_path = ppd.channel_log_path("substack")
    existing = ppd.load_json(log_path).get("posts", {}).get(key)

    if args.check:
        if ppd.is_blocking_distribution_entry("substack", existing):
            print(json.dumps({"slug": args.slug, "key": key, "receipt": existing}, ensure_ascii=False, indent=2))
            return 0
        print(json.dumps({"slug": args.slug, "key": key, "receipt": None}, ensure_ascii=False))
        return 1

    errors = []
    if not SUBSTACK_URL_RE.match(args.substack_url):
        errors.append("--substack-url must look like https://<pub>.substack.com/p/<slug>")
    if args.draft_id <= 0:
        errors.append("--draft-id is required")
    if args.note_url and not NOTE_URL_RE.match(args.note_url):
        errors.append("--note-url must look like https://substack.com/note/c-<id>")
    if not args.note_url and not args.no_note:
        errors.append("--note-url is required (or --no-note '<reason>' for an explicit exception)")
    if ppd.is_blocking_distribution_entry("substack", existing) and not args.force:
        errors.append(f"a receipt already exists for {key}; pass --force to replace it")
    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        return 2

    if not args.no_live_check:
        code = public_status(args.substack_url)
        if code != 200:
            print(f"error: {args.substack_url} answered {code or 'no response'}, not 200", file=sys.stderr)
            return 3

    summary = {
        "slug": args.slug,
        "url": key,
        "substack_url": args.substack_url,
        "draft_id": args.draft_id,
        "note_url": args.note_url,
        "emailed": args.emailed == "yes",
        "via": "browser-pane (scripts/substack_pane_push.js)",
    }
    if args.no_note:
        summary["no_note_reason"] = args.no_note
    valley.record_crosspost(log_path, key, "publish", summary)
    print(json.dumps({"recorded": key, "log": str(log_path), "response": summary}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
