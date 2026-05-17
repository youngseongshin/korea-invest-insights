#!/usr/bin/env python3
"""Run post-publish distribution hooks for Korea Invest Insights.

The blog's canonical publish path is still GitHub Pages. This script is the
local distribution stage that runs after a post is live. It intentionally keeps
cookie-backed destinations on the user's Mac instead of GitHub Actions.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
import sys
from pathlib import Path

import valley_auto_publish
import valley_crosspost as valley


DEFAULT_REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = Path.home() / ".config" / "korea-invest-insights" / "valley.env"
DEFAULT_DATA_DIR = Path.home() / ".local" / "share" / "korea-invest-insights"
OPENCLAW_TOOLS = Path.home() / ".openclaw" / "workspace" / "tools"
DEFAULT_CHANNELS = ["telegram", "botmadang", "substack", "valley"]
SUPPORTED_CHANNELS = set(DEFAULT_CHANNELS)
UNIFIED_WATERMARK_KEY = "unifiedDistributionActivatedAt"


def parse_channels(raw: str) -> list[str]:
    channels = [part.strip().lower() for part in raw.split(",") if part.strip()]
    unknown = sorted(set(channels) - SUPPORTED_CHANNELS)
    if unknown:
        raise SystemExit(f"Unsupported distribution channel(s): {', '.join(unknown)}")
    return channels or list(DEFAULT_CHANNELS)


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


def parse_iso_timestamp(value: object) -> float | None:
    if not value:
        return None
    try:
        parsed = dt.datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.timestamp()


def load_json(path: Path) -> dict:
    path = path.expanduser()
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def save_json(path: Path, data: dict) -> None:
    path = path.expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def post_slug(post: dict) -> str:
    path = Path(str(post["path"]))
    return path.parent.name


def git_added_timestamp(repo_root: Path, path: Path) -> float | None:
    try:
        relative_path = str(path.resolve().relative_to(repo_root.resolve()))
    except ValueError:
        relative_path = str(path)

    completed = subprocess.run(
        ["git", "log", "--diff-filter=A", "--format=%ct", "-1", "--", relative_path],
        cwd=repo_root,
        check=False,
        text=True,
        capture_output=True,
        timeout=10,
    )
    if completed.returncode != 0:
        return None
    output = completed.stdout.strip().splitlines()
    if not output:
        return None
    try:
        return float(output[0])
    except ValueError:
        return None


def distribution_sort_timestamp(post: dict, path: Path, repo_root: Path) -> float:
    added_at = git_added_timestamp(repo_root, path)
    if added_at is not None:
        return added_at
    parsed = valley.parse_date(post.get("date"))
    return valley.date_sort_key(parsed, path.stat().st_mtime)


def channel_log_path(channel: str) -> Path:
    return DEFAULT_DATA_DIR / f"{channel}_distribution_log.json"


def channel_state_path(channel: str) -> Path:
    return DEFAULT_DATA_DIR / f"{channel}_auto_publish_state.json"


def discover_distribution_candidates(
    repo_root: Path,
    lang: str,
    since_days: int,
    log_path: Path,
    min_timestamp: float | None,
) -> list[dict]:
    post_paths = sorted((repo_root / "content" / "post").glob(f"*/index.{lang}.md"))
    log = valley_auto_publish.read_crosspost_log(log_path)
    sent_urls = set(log.get("posts", {}).keys())
    cutoff = dt.datetime.now(dt.timezone.utc).timestamp() - since_days * 86400 if since_days > 0 else None
    candidates: list[tuple[float, dict]] = []

    for path in post_paths:
        post = valley.load_post(path)
        if post["front_matter"].get("draft") is True:
            continue
        if post["canonical_url"] in sent_urls:
            continue
        timestamp = distribution_sort_timestamp(post, path, repo_root)
        if cutoff is not None and timestamp < cutoff:
            continue
        if min_timestamp is not None and timestamp < min_timestamp:
            continue
        candidates.append((timestamp, post))

    candidates.sort(key=lambda item: item[0])
    return [post for _, post in candidates]


def discover_channel_candidates(args: argparse.Namespace, channel: str) -> tuple[list[dict], dict | None]:
    state_path = channel_state_path(channel)
    state = load_json(state_path)
    started_at = parse_iso_timestamp(state.get("startedAt"))
    unified_started_at = parse_iso_timestamp(state.get(UNIFIED_WATERMARK_KEY))

    if not args.dry_run and started_at is None and not args.allow_backfill:
        now = dt.datetime.now(dt.timezone.utc).isoformat()
        state.update({"startedAt": now, "backfill": False, UNIFIED_WATERMARK_KEY: now})
        save_json(state_path, state)
        return [], {
            "status": "initialized",
            "reason": "Created first-run watermark; existing posts were not backfilled",
            "statePath": str(state_path),
            "startedAt": now,
        }

    if not args.dry_run and unified_started_at is None and not args.allow_backfill:
        now = dt.datetime.now(dt.timezone.utc).isoformat()
        state[UNIFIED_WATERMARK_KEY] = now
        save_json(state_path, state)
        return [], {
            "status": "initialized",
            "reason": "Created unified distribution watermark; existing posts were not backfilled",
            "statePath": str(state_path),
            UNIFIED_WATERMARK_KEY: now,
        }

    watermarks = [value for value in (started_at, unified_started_at) if value is not None]
    min_timestamp = max(watermarks) if watermarks else None

    candidates = discover_distribution_candidates(
        Path(args.repo_root).resolve(),
        args.lang,
        args.since_days,
        channel_log_path(channel),
        min_timestamp,
    )
    return candidates, None


def run_external(command: list[str], args: argparse.Namespace) -> tuple[int, str]:
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{OPENCLAW_TOOLS}:{env.get('PYTHONPATH', '')}"
    if args.dry_run:
        return 0, "dry_run"
    completed = subprocess.run(
        command,
        cwd=Path(args.repo_root).resolve(),
        env=env,
        check=False,
        text=True,
        capture_output=True,
        timeout=args.channel_timeout,
    )
    output = "\n".join(part for part in [completed.stdout.strip(), completed.stderr.strip()] if part)
    if output:
        print(output)
    return completed.returncode, output[-500:]


def record_channel(channel: str, post: dict, action: str, summary: dict) -> None:
    valley.record_crosspost(channel_log_path(channel), post["canonical_url"], action, summary)


def run_telegram_for_post(post: dict, args: argparse.Namespace) -> dict:
    slug = post_slug(post)
    if args.dry_run:
        return {"status": "would_notify", "slug": slug, "url": post["canonical_url"]}
    code, tail = run_external(
        [
            sys.executable,
            str(OPENCLAW_TOOLS / "blog_channel_notify.py"),
            "--slug",
            slug,
        ],
        args,
    )
    if code == 0:
        summary = {"slug": slug, "url": post["canonical_url"]}
        record_channel("telegram", post, "notify", summary)
        return {"status": "notified", **summary}
    return {"status": "error", "slug": slug, "exitCode": code, "tail": tail}


def run_botmadang_for_post(post: dict, args: argparse.Namespace) -> dict:
    slug = post_slug(post)
    if args.dry_run:
        return {"status": "would_publish", "slug": slug, "url": post["canonical_url"]}
    code, tail = run_external(
        [
            sys.executable,
            str(OPENCLAW_TOOLS / "blog_botmadang_notify.py"),
            slug,
            "--submadang",
            args.botmadang_submadang,
        ],
        args,
    )
    if code == 0:
        summary = {"slug": slug, "url": post["canonical_url"]}
        record_channel("botmadang", post, "publish", summary)
        return {"status": "published", **summary}
    return {"status": "error", "slug": slug, "exitCode": code, "tail": tail}


def run_substack_for_post(post: dict, args: argparse.Namespace) -> dict:
    slug = post_slug(post)
    english_path = Path(args.repo_root).resolve() / "content" / "post" / slug / "index.en.md"
    if not english_path.exists():
        summary = {"slug": slug, "reason": "index.en.md missing"}
        if not args.dry_run:
            record_channel("substack", post, "skip_no_english", summary)
        return {"status": "skipped", **summary}

    if args.dry_run:
        return {"status": "would_publish", "slug": slug, "path": str(english_path)}

    script = (
        "import json, re; "
        "from pathlib import Path; "
        "from substack_publisher import publish_to_substack; "
        "from substack_notes import post_note_for_post; "
        f"p=Path({str(english_path)!r}); md=p.read_text(encoding='utf-8'); "
        f"slug={slug!r}; "
        "result=publish_to_substack(md, slug); "
        "url=result.get('url',''); "
        "title=(re.search(r'^title:\\s*\"?(.+?)\"?\\s*$', md, re.M) or [None, slug])[1].strip('\"'); "
        "desc_m=re.search(r'^description:\\s*\"?(.+?)\"?\\s*$', md, re.M); "
        "desc=desc_m.group(1).strip('\"') if desc_m else ''; "
        "note=post_note_for_post(slug, title, desc, url) if url else {}; "
        "print(json.dumps({'substack': result, 'note': note}, ensure_ascii=False))"
    )
    code, tail = run_external([sys.executable, "-c", script], args)
    if code == 0:
        summary = {"slug": slug, "url": post["canonical_url"]}
        record_channel("substack", post, "publish", summary)
        return {"status": "published", **summary}
    return {"status": "error", "slug": slug, "exitCode": code, "tail": tail}


def run_candidate_channel(channel: str, args: argparse.Namespace) -> int:
    candidates, initialized = discover_channel_candidates(args, channel)
    results: list[dict] = []
    if initialized:
        results.append(initialized)

    processed = 0
    for post in candidates:
        if processed >= args.max_posts:
            break

        live_ok = True
        live_detail = "not checked"
        if args.require_live:
            live_ok, live_detail = valley_auto_publish.is_live(post["canonical_url"])
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

        # The launchd poller and manual publish commands can be active at the
        # same time. Re-read the channel log after the live check so a stale
        # candidate list cannot notify or publish the same post twice.
        if not args.dry_run:
            latest_log = load_json(channel_log_path(channel))
            if post["canonical_url"] in latest_log.get("posts", {}):
                results.append(
                    {
                        "status": "skipped_already_distributed",
                        "title": post["title"],
                        "url": post["canonical_url"],
                    }
                )
                continue

        if channel == "telegram":
            result = run_telegram_for_post(post, args)
        elif channel == "botmadang":
            result = run_botmadang_for_post(post, args)
        elif channel == "substack":
            result = run_substack_for_post(post, args)
        else:
            raise RuntimeError(f"unsupported candidate channel: {channel}")
        result.setdefault("title", post["title"])
        result.setdefault("url", post["canonical_url"])
        results.append(result)
        processed += 1

        if result.get("status") == "error":
            print(json.dumps({"channel": channel, "status": "failed", "results": results}, ensure_ascii=False, indent=2))
            return 1

    print(
        json.dumps(
            {
                "channel": channel,
                "status": "ok",
                "dryRun": args.dry_run,
                "candidateCount": len(candidates),
                "processedCount": processed,
                "results": results,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run post-publish distribution channels after the blog URL is live."
    )
    parser.add_argument("--repo-root", default=str(DEFAULT_REPO_ROOT))
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH))
    parser.add_argument(
        "--channels",
        default=",".join(DEFAULT_CHANNELS),
        help="Comma-separated channels to run after the blog URL is live. Default: telegram,botmadang,substack,valley.",
    )
    parser.add_argument("--lang", default="ko")
    parser.add_argument("--since-days", type=int, default=14)
    parser.add_argument("--max-posts", type=int, default=3)
    parser.add_argument("--body-mode", choices=("teaser", "full", "auto"), default="auto")
    parser.add_argument("--botmadang-submadang", default="finance")
    parser.add_argument("--channel-timeout", type=int, default=240)
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

    for channel in ("telegram", "botmadang", "substack"):
        if channel in channels:
            code = run_candidate_channel(channel, args)
            results.append({"channel": channel, "exitCode": code})

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
