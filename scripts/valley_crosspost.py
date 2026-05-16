#!/usr/bin/env python3
"""Prepare or send a Korea Invest Insights post to Valley Space.

The Valley web app currently publishes articles through session-backed private
endpoints, not a documented public API. This script therefore defaults to a
local preview and only writes to Valley when explicit credentials are provided
through environment variables.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import textwrap
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


SITE_BASE_URL = "https://koreainvestinsights.com"
VALLEY_API_BASE_URL = "https://api.valley.town"
DEFAULT_LOG_PATH = (
    Path.home()
    / ".local"
    / "share"
    / "korea-invest-insights"
    / "valley_crosspost_log.json"
)
LANG_PREFIXES = {"en": "", "ko": "/ko", "es": "/es", "vi": "/vi", "fr": "/fr", "ja": "/ja", "zh": "/zh"}
SUMMARY_HEADINGS = (
    "핵심 요약",
    "TL;DR",
    "Key Takeaways",
    "核心摘要",
    "Points clés",
    "Resumen clave",
    "要点",
)
AUTO_FULL_CATEGORIES = {
    "Market-Outlook",
    "Macro-Insight",
    "Market-Commentary",
    "Daily-Intelligence",
}
AUTO_TEASER_CATEGORIES = {
    "Company-Deep-Dive",
    "Sector-Deep-Dive",
    "Stock-Analysis",
    "Why-Korea",
    "Analyst-Report-Cover",
}
AUTO_FULL_SLUG_PREFIXES = (
    "kr-daily-wrap-",
    "kospi-",
    "google-io-",
)
AUTO_FULL_MAX_CHARS = 9000
AUTO_FULL_MAX_TABLE_LINES = 8


class ValleyCrosspostError(RuntimeError):
    pass


def split_front_matter(raw: str) -> tuple[dict[str, Any], str]:
    if not raw.startswith("---\n"):
        return {}, raw
    end = raw.find("\n---", 4)
    if end == -1:
        return {}, raw
    front_matter = raw[4:end].strip("\n")
    body = raw[end + len("\n---") :].lstrip("\n")
    return parse_simple_yaml(front_matter), body


def parse_simple_yaml(front_matter: str) -> dict[str, Any]:
    """Parse the small YAML subset used in Hugo front matter."""
    data: dict[str, Any] = {}
    current_key: str | None = None

    for line in front_matter.splitlines():
        raw_line = line.rstrip()
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        item_match = re.match(r"^\s*-\s+(.+?)\s*$", raw_line)
        if item_match and current_key:
            data.setdefault(current_key, []).append(clean_scalar(item_match.group(1)))
            continue

        key_match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", raw_line)
        if not key_match:
            current_key = None
            continue

        key, value = key_match.group(1), (key_match.group(2) or "").strip()
        if value == "":
            data[key] = []
            current_key = key
            continue

        current_key = None
        data[key] = parse_scalar_or_list(value)

    return data


def parse_scalar_or_list(value: str) -> Any:
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [clean_scalar(part.strip()) for part in split_csv_like(inner)]
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    return clean_scalar(value)


def split_csv_like(value: str) -> list[str]:
    parts: list[str] = []
    current: list[str] = []
    quote: str | None = None
    escaped = False
    for char in value:
        if escaped:
            current.append(char)
            escaped = False
            continue
        if char == "\\":
            current.append(char)
            escaped = True
            continue
        if quote:
            current.append(char)
            if char == quote:
                quote = None
            continue
        if char in {"'", '"'}:
            current.append(char)
            quote = char
            continue
        if char == ",":
            parts.append("".join(current))
            current = []
            continue
        current.append(char)
    parts.append("".join(current))
    return parts


def clean_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value.replace('\\"', '"').replace("\\'", "'").strip()


def load_post(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    front_matter, body = split_front_matter(raw)
    slug = front_matter.get("slug") or path.parent.name
    lang = path.stem.split(".")[-1] if "." in path.name else "en"
    title = front_matter.get("title") or slug.replace("-", " ").title()
    description = front_matter.get("description") or ""
    tags = front_matter.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    categories = front_matter.get("categories") or []
    if isinstance(categories, str):
        categories = [categories]

    return {
        "path": path,
        "front_matter": front_matter,
        "body": body,
        "slug": slug,
        "lang": lang,
        "title": title,
        "description": description,
        "tags": tags,
        "categories": categories,
        "date": front_matter.get("date"),
        "canonical_url": canonical_url(slug, lang),
    }


def canonical_url(slug: str, lang: str) -> str:
    prefix = LANG_PREFIXES.get(lang, f"/{lang}")
    return f"{SITE_BASE_URL}{prefix}/post/{slug}/"


def find_latest_post(content_root: Path, lang: str) -> Path:
    candidates: list[tuple[float, float, Path]] = []
    pattern = f"content/post/*/index.{lang}.md"
    for path in content_root.glob(pattern):
        post = load_post(path)
        if post["front_matter"].get("draft") is True:
            continue
        date_value = post["date"]
        parsed_date = parse_date(date_value)
        candidates.append((date_sort_key(parsed_date, path.stat().st_mtime), path.stat().st_mtime, path))
    if not candidates:
        raise ValleyCrosspostError(f"No posts found for language: {lang}")
    candidates.sort(reverse=True)
    return candidates[0][2]


def parse_date(value: Any) -> dt.datetime | None:
    if not value:
        return None
    text = str(value).strip().strip('"')
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S%Z", "%Y-%m-%d"):
        try:
            return dt.datetime.strptime(text, fmt)
        except ValueError:
            continue
    try:
        return dt.datetime.fromisoformat(text)
    except ValueError:
        return None


def date_sort_key(value: dt.datetime | None, fallback_mtime: float) -> float:
    if value is None:
        return fallback_mtime
    if value.tzinfo is None:
        value = value.replace(tzinfo=dt.timezone.utc)
    return value.timestamp()


def extract_summary(body: str, limit: int = 10) -> list[str]:
    lines = body.splitlines()
    start = None
    for index, line in enumerate(lines):
        stripped = line.strip().lstrip("#").strip()
        if any(stripped.lower() == heading.lower() for heading in SUMMARY_HEADINGS):
            start = index + 1
            break
    if start is not None:
        picked: list[str] = []
        for line in lines[start:]:
            stripped = line.strip()
            if stripped.startswith("## ") and picked:
                break
            if not stripped:
                continue
            if stripped.startswith(("-", "*", "1.")) or stripped.startswith("|"):
                picked.append(normalize_social_line(stripped))
            if len(picked) >= limit:
                break
        if picked:
            return picked

    paragraphs: list[str] = []
    buffer: list[str] = []
    for line in body.splitlines():
        stripped = strip_markdown_noise(line.strip())
        if not stripped:
            if buffer:
                paragraphs.append(normalize_social_line(" ".join(buffer)))
                buffer = []
            continue
        if stripped.startswith("#") or stripped.startswith(">"):
            continue
        buffer.append(stripped)
        if len(" ".join(buffer)) > 450:
            paragraphs.append(normalize_social_line(" ".join(buffer)))
            buffer = []
        if len(paragraphs) >= 3:
            break
    if buffer and len(paragraphs) < 3:
        paragraphs.append(normalize_social_line(" ".join(buffer)))
    return paragraphs[:3]


def normalize_social_line(line: str) -> str:
    line = line.strip()
    line = re.sub(r"^[*-]\s+", "- ", line)
    line = re.sub(r"^(\d+)\.\s+", r"\1. ", line)
    line = re.sub(r"\*\*([^*]+)\*\*", r"\1", line)
    line = re.sub(r"`([^`]+)`", r"\1", line)
    line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", line)
    return line


def strip_markdown_noise(line: str) -> str:
    line = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", line)
    line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", line)
    line = line.strip("*_` ")
    return line


def resolve_body_mode(post: dict[str, Any], body_mode: str) -> str:
    if body_mode != "auto":
        return body_mode

    explicit = str(post["front_matter"].get("valley_body_mode", "")).strip().lower()
    if explicit in {"teaser", "full"}:
        return explicit

    body = post["body"]
    body_chars = len(body)
    table_lines = sum(1 for line in body.splitlines() if line.strip().startswith("|"))
    categories = {str(category) for category in post.get("categories", [])}

    if categories & AUTO_TEASER_CATEGORIES:
        return "teaser"
    if body_chars > AUTO_FULL_MAX_CHARS or table_lines > AUTO_FULL_MAX_TABLE_LINES:
        return "teaser"
    if categories & AUTO_FULL_CATEGORIES:
        return "full"
    if post["slug"].startswith(AUTO_FULL_SLUG_PREFIXES):
        return "full"
    return "teaser"


def build_body(post: dict[str, Any], body_mode: str) -> str:
    body_mode = resolve_body_mode(post, body_mode)
    if post["lang"] == "ko":
        source_label = "원문 전체 읽기"
        summary_label = "핵심 요약"
        footer = "표, 내부 링크, 전체 맥락은 Korea Invest Insights 원문에서 확인할 수 있습니다."
    else:
        source_label = "Read the full post"
        summary_label = "Key takeaways"
        footer = "Tables, internal links, and the full context are available on Korea Invest Insights."

    if body_mode == "full":
        source = f"{source_label}\n{post['canonical_url']}"
        return f"{source}\n\n---\n\n{post['body'].strip()}\n\n---\n\n{footer}"

    summary = extract_summary(post["body"])
    parts = []
    if post["description"]:
        parts.append(post["description"].strip())
    parts.extend(
        [
            f"{source_label}\n{post['canonical_url']}",
            summary_label,
        ]
    )
    parts.extend(summary)
    parts.append(footer)
    return "\n\n".join(part for part in parts if part)


def text_content(text: str) -> list[dict[str, Any]]:
    url_match = re.search(r"https?://\S+", text)
    if not url_match:
        return [{"type": "text", "text": text}]

    content: list[dict[str, Any]] = []
    before = text[: url_match.start()]
    url = url_match.group(0)
    after = text[url_match.end() :]
    if before:
        content.append({"type": "text", "text": before})
    content.append(
        {
            "type": "text",
            "text": url,
            "marks": [
                {
                    "type": "link",
                    "attrs": {
                        "href": url,
                        "target": "_blank",
                        "rel": "noopener noreferrer nofollow",
                    },
                }
            ],
        }
    )
    if after:
        content.append({"type": "text", "text": after})
    return content


def paragraph_node(text: str) -> dict[str, Any]:
    return {"type": "paragraph", "content": text_content(text)}


def heading_node(text: str, level: int = 2) -> dict[str, Any]:
    return {"type": "heading", "attrs": {"level": level}, "content": [{"type": "text", "text": text}]}


def bullet_list_node(lines: list[str]) -> dict[str, Any]:
    return {
        "type": "bulletList",
        "content": [
            {
                "type": "listItem",
                "content": [paragraph_node(line.lstrip("-*").strip())],
            }
            for line in lines
            if line.lstrip("-*").strip()
        ],
    }


def text_to_tiptap_doc(text: str) -> dict[str, Any]:
    content: list[dict[str, Any]] = []
    pending_bullets: list[str] = []

    def flush_bullets() -> None:
        nonlocal pending_bullets
        if pending_bullets:
            content.append(bullet_list_node(pending_bullets))
            pending_bullets = []

    for block in re.split(r"\n{2,}", text.strip()):
        block = block.strip()
        if not block:
            continue
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if len(lines) > 1 and all(line.startswith(("- ", "* ")) for line in lines):
            pending_bullets.extend(lines)
            continue
        if len(lines) == 1 and lines[0].startswith(("- ", "* ")):
            pending_bullets.extend(lines)
            continue
        flush_bullets()
        if block.startswith("#"):
            level = min(len(block) - len(block.lstrip("#")), 3)
            heading_text = block.lstrip("#").strip()
            content.append(heading_node(heading_text, level))
        elif block.strip() in SUMMARY_HEADINGS:
            content.append(heading_node(block.strip(), 2))
        elif block.strip() == "---":
            content.append({"type": "horizontalRule"})
        elif len(lines) == 2 and lines[1].startswith("http"):
            content.append(heading_node(lines[0], 3))
            content.append(paragraph_node(lines[1]))
        else:
            paragraph_text = re.sub(r"\s*\n\s*", "\n", block)
            content.append(paragraph_node(paragraph_text))
    flush_bullets()
    return {"type": "doc", "content": content or [{"type": "paragraph"}]}


def build_valley_payload(post: dict[str, Any], body_mode: str, category_id: str | None) -> dict[str, Any]:
    resolved_body_mode = resolve_body_mode(post, body_mode)
    body = build_body(post, resolved_body_mode)
    payload: dict[str, Any] = {
        "type": "POST",
        "title": post["title"],
        "content": body,
        "contentJson": json.dumps(text_to_tiptap_doc(body), ensure_ascii=False),
        "attachments": [],
        "tags": valley_tags(post["tags"]),
    }
    if category_id:
        payload["postCategoryId"] = category_id
    return payload


def valley_tags(tags: list[str]) -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []
    seen: set[str] = set()
    for tag in tags:
        key = str(tag).strip().lstrip("#")
        if not key or key in seen:
            continue
        seen.add(key)
        normalized.append({"type": "KEYWORD", "key": key})
        if len(normalized) >= 10:
            break
    return normalized


def api_request(method: str, endpoint: str, body: dict[str, Any] | None, api_base: str) -> dict[str, Any]:
    cookie = os.environ.get("VALLEY_COOKIE", "").strip()
    bearer = os.environ.get("VALLEY_API_TOKEN", "").strip()
    if not cookie and not bearer:
        raise ValleyCrosspostError(
            "Valley credentials are missing. Set VALLEY_COOKIE for local draft mode "
            "or VALLEY_API_TOKEN if Valley provides an official token."
        )

    data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
    request = urllib.request.Request(f"{api_base.rstrip('/')}{endpoint}", data=data, method=method)
    request.add_header("Accept", "application/json")
    request.add_header("Content-Type", "application/json")
    request.add_header("Origin", "https://www.valley.town")
    request.add_header("Referer", "https://www.valley.town/space/publish/articles")
    request.add_header("User-Agent", "korea-invest-insights-valley-crosspost/0.1")
    if cookie:
        request.add_header("Cookie", cookie)
    if bearer:
        request.add_header("Authorization", f"Bearer {bearer}")

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            response_body = response.read().decode("utf-8")
            return json.loads(response_body) if response_body else {}
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise ValleyCrosspostError(f"Valley API {method} {endpoint} failed: HTTP {error.code} {detail}") from error
    except urllib.error.URLError as error:
        raise ValleyCrosspostError(f"Valley API {method} {endpoint} failed: {error}") from error


def load_log(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"posts": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def save_log(path: Path, log: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def record_crosspost(log_path: Path, canonical_url: str, mode: str, response: dict[str, Any]) -> None:
    log = load_log(log_path)
    log.setdefault("posts", {})[canonical_url] = {
        "mode": mode,
        "at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "response": response,
    }
    save_log(log_path, log)


def summarize_response(response: dict[str, Any]) -> dict[str, Any]:
    post = response.get("post") or response.get("postDraft") or response
    return {
        "id": post.get("id"),
        "title": post.get("title") or post.get("payload", {}).get("title"),
        "createdAt": post.get("createdAt"),
        "updatedAt": post.get("updatedAt"),
    }


def list_categories(api_base: str) -> None:
    response = api_request("GET", "/post/categories", None, api_base)
    categories = response.get("postCategories") or response.get("categories") or response
    print(json.dumps(categories, ensure_ascii=False, indent=2))


def run(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    api_base = args.api_base.rstrip("/")

    if args.mode == "categories":
        list_categories(api_base)
        return 0

    post_path = Path(args.post).resolve() if args.post else find_latest_post(repo_root, args.lang)
    post = load_post(post_path)
    payload = build_valley_payload(post, args.body_mode, args.category_id)
    outbound_body = (
        {"postDraft": {"postType": "POST", "payload": payload}}
        if args.mode == "draft"
        else {"post": payload}
    )

    if args.mode == "preview":
        print(json.dumps({"post": post_metadata(post), "valleyRequest": outbound_body}, ensure_ascii=False, indent=2))
        return 0

    log_path = Path(args.log_path).expanduser()
    log = load_log(log_path)
    if post["canonical_url"] in log.get("posts", {}) and not args.force:
        raise ValleyCrosspostError(
            f"Already cross-posted: {post['canonical_url']} "
            f"(use --force to send again)"
        )

    if args.mode == "publish":
        if not args.confirm_publish:
            raise ValleyCrosspostError("Publishing requires --confirm-publish.")
        if not args.category_id:
            raise ValleyCrosspostError("Publishing requires --category-id.")
        response = api_request("POST", "/post/posts", outbound_body, api_base)
    elif args.mode == "draft":
        response = api_request("POST", "/post/drafts", outbound_body, api_base)
    elif args.mode == "update":
        if not args.confirm_update:
            raise ValleyCrosspostError("Updating requires --confirm-update.")
        post_id = args.post_id or log.get("posts", {}).get(post["canonical_url"], {}).get("response", {}).get("id")
        if not post_id:
            raise ValleyCrosspostError("Updating requires --post-id or an existing id in the local crosspost log.")
        if not payload.get("postCategoryId"):
            raise ValleyCrosspostError("Updating requires --category-id.")
        update_body = {
            "update": {
                "title": payload["title"],
                "content": payload["content"],
                "contentJson": payload["contentJson"],
                "attachments": payload.get("attachments", []),
                "tags": payload.get("tags", []),
                "postCategoryId": payload.get("postCategoryId"),
            },
        }
        response = api_request("PUT", f"/post/posts/{post_id}", update_body, api_base)
    else:
        raise ValleyCrosspostError(f"Unknown mode: {args.mode}")

    summary = summarize_response(response)
    record_crosspost(log_path, post["canonical_url"], args.mode, summary)
    print(json.dumps({"sent": args.mode, "source": post_metadata(post), "valley": summary}, ensure_ascii=False, indent=2))
    return 0


def post_metadata(post: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": post["title"],
        "lang": post["lang"],
        "path": str(post["path"]),
        "canonicalUrl": post["canonical_url"],
        "tags": post["tags"],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Prepare, draft, or publish a Hugo post to Valley Space.",
        epilog=textwrap.dedent(
            """\
            Examples:
              Preview latest Korean post:
                scripts/valley_crosspost.py --latest --lang ko

              Create a Valley draft locally:
                VALLEY_COOKIE='...' scripts/valley_crosspost.py --latest --lang ko --mode draft

              Update an existing Valley post from the local log:
                VALLEY_COOKIE='...' scripts/valley_crosspost.py --post content/post/.../index.ko.md --mode update --confirm-update

              List Valley categories:
                VALLEY_COOKIE='...' scripts/valley_crosspost.py --mode categories
            """
        ),
    )
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--post", help="Path to a Hugo Markdown file, e.g. content/post/.../index.ko.md")
    source.add_argument("--latest", action="store_true", help="Use the latest published post for --lang")
    parser.add_argument("--lang", default="ko", help="Language for --latest (default: ko)")
    parser.add_argument("--repo-root", default=".", help="Repository root (default: current directory)")
    parser.add_argument("--mode", choices=("preview", "draft", "publish", "update", "categories"), default="preview")
    parser.add_argument("--body-mode", choices=("auto", "teaser", "full"), default="teaser")
    parser.add_argument("--category-id", default=os.environ.get("VALLEY_POST_CATEGORY_ID"))
    parser.add_argument("--api-base", default=os.environ.get("VALLEY_API_BASE", VALLEY_API_BASE_URL))
    parser.add_argument("--log-path", default=str(DEFAULT_LOG_PATH))
    parser.add_argument("--force", action="store_true", help="Send even if canonical URL exists in local crosspost log")
    parser.add_argument("--confirm-publish", action="store_true", help="Required for mode=publish")
    parser.add_argument("--confirm-update", action="store_true", help="Required for mode=update")
    parser.add_argument("--post-id", help="Valley post id for mode=update. Defaults to id stored in local log.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if not args.post and not args.latest and args.mode != "categories":
        args.latest = True
    try:
        return run(args)
    except ValleyCrosspostError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
