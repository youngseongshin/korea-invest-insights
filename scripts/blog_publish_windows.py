#!/usr/bin/env python
"""Windows entrypoint for the OpenClaw Korea Invest Insights publish pipeline."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def default_openclaw_tools(root: Path) -> Path:
    candidates = [
        root.parent / "openclaw-workspace" / "workspace" / "tools",
        root.parent / "openclaw-workspace" / "tools",
        Path.home() / ".openclaw" / "workspace" / "tools",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()
    return candidates[0].resolve()


def configure_environment(root: Path, tools: Path) -> None:
    os.environ.setdefault("KII_REPO_ROOT", str(root))
    os.environ.setdefault("KOREA_INVEST_INSIGHTS_ROOT", str(root))
    os.environ.setdefault("KII_SCRIPTS", str(root / "scripts"))
    os.environ.setdefault("OPENCLAW_TOOLS", str(tools))
    os.environ.setdefault("PYTHONUTF8", "1")
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    for path in [tools, root / "scripts"]:
        text = str(path)
        if text not in sys.path:
            sys.path.insert(0, text)


def read_markdown(path: str | None) -> str | None:
    if not path:
        return None
    return Path(path).expanduser().resolve().read_text(encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Run the OpenClaw blog publish pipeline against this Windows clone. "
            "Defaults are conservative: vault sync, Substack, Telegram DM, "
            "Botmadang, and Valley are skipped unless explicitly enabled."
        )
    )
    parser.add_argument("--english-md", required=True, help="Path to English Hugo markdown with front matter.")
    parser.add_argument("--korean-md", help="Optional Korean Hugo markdown with matching slug.")
    parser.add_argument("--slug", help="Override slug. Defaults to front matter slug.")
    parser.add_argument("--today", help="Publish date YYYY-MM-DD. Defaults to today.")
    parser.add_argument("--commit-prefix", default="blog")
    parser.add_argument("--openclaw-tools", help="Path to OpenClaw workspace tools.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-translate", action="store_true")
    parser.add_argument("--include-vault", action="store_true", help="Allow vault write/sync. Default is skip on Windows.")
    parser.add_argument("--include-substack", action="store_true")
    parser.add_argument("--include-channel", action="store_true", help="Allow Telegram channel notification.")
    parser.add_argument("--include-dm", action="store_true", help="Allow Telegram DM notification.")
    parser.add_argument("--include-botmadang", action="store_true")
    parser.add_argument("--include-valley", action="store_true")
    parser.add_argument("--humanize-korean-output", action=argparse.BooleanOptionalAction, default=None)
    return parser


def main() -> int:
    root = repo_root()
    args = build_parser().parse_args()
    tools = Path(args.openclaw_tools).expanduser().resolve() if args.openclaw_tools else default_openclaw_tools(root)
    configure_environment(root, tools)

    from blog_publish_pipeline import BlogPublishPipeline

    english_md = read_markdown(args.english_md)
    korean_md = read_markdown(args.korean_md)
    publish_date = date.fromisoformat(args.today) if args.today else None

    pipeline = BlogPublishPipeline(
        english_md=english_md,
        korean_md=korean_md,
        slug=args.slug,
        today=publish_date,
        commit_prefix=args.commit_prefix,
        humanize_korean_output=args.humanize_korean_output,
    )
    result = pipeline.run(
        skip_translate=args.skip_translate,
        skip_vault=not args.include_vault,
        skip_substack=not args.include_substack,
        skip_channel=not args.include_channel,
        skip_dm=not args.include_dm,
        skip_botmadang=not args.include_botmadang,
        skip_valley=not args.include_valley,
        dry_run=args.dry_run,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result.get("errors") else 0


if __name__ == "__main__":
    raise SystemExit(main())
