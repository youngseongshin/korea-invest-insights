#!/usr/bin/env python3
"""Run post-publish distribution hooks for Korea Invest Insights.

The blog's canonical publish path is still GitHub Pages. This script is the
local distribution stage that runs after a post is live. It intentionally keeps
cookie-backed destinations on the user's Mac instead of GitHub Actions.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


DEFAULT_REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = Path.home() / ".config" / "korea-invest-insights" / "valley.env"
SUPPORTED_CHANNELS = {"valley"}


def parse_channels(raw: str) -> list[str]:
    channels = [part.strip().lower() for part in raw.split(",") if part.strip()]
    unknown = sorted(set(channels) - SUPPORTED_CHANNELS)
    if unknown:
        raise SystemExit(f"Unsupported distribution channel(s): {', '.join(unknown)}")
    return channels or ["valley"]


def run_valley(args: argparse.Namespace) -> int:
    command = [
        sys.executable,
        str(Path(__file__).resolve().parent / "valley_auto_publish.py"),
        "--repo-root",
        str(Path(args.repo_root).resolve()),
        "--config",
        str(Path(args.config).expanduser()),
        "--lang",
        args.lang,
        "--since-days",
        str(args.since_days),
        "--max-posts",
        str(args.max_posts),
        "--body-mode",
        args.body_mode,
    ]
    if args.require_live:
        command.append("--require-live")
    if args.allow_backfill:
        command.append("--allow-backfill")
    if args.dry_run:
        command.append("--dry-run")

    completed = subprocess.run(command, cwd=Path(args.repo_root).resolve(), check=False)
    return completed.returncode


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run post-publish distribution channels after the blog URL is live."
    )
    parser.add_argument("--repo-root", default=str(DEFAULT_REPO_ROOT))
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH))
    parser.add_argument("--channels", default="valley", help="Comma-separated channels. Currently: valley")
    parser.add_argument("--lang", default="ko")
    parser.add_argument("--since-days", type=int, default=14)
    parser.add_argument("--max-posts", type=int, default=3)
    parser.add_argument("--body-mode", choices=("teaser", "full", "auto"), default="auto")
    parser.add_argument("--require-live", dest="require_live", action="store_true", default=True)
    parser.add_argument("--no-require-live", dest="require_live", action="store_false")
    parser.add_argument("--allow-backfill", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    channels = parse_channels(args.channels)
    results: list[dict[str, int | str]] = []

    if "valley" in channels:
        code = run_valley(args)
        results.append({"channel": "valley", "exitCode": code})
    else:
        code = 0

    status = "completed" if all(int(item["exitCode"]) == 0 for item in results) else "failed"
    print(
        json.dumps(
            {
                "stage": "post_publish_distribution",
                "status": status,
                "dryRun": args.dry_run,
                "channels": results,
            },
            ensure_ascii=False,
        )
    )
    return 0 if status == "completed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
