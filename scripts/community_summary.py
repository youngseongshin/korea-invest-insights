#!/usr/bin/env python3
"""Shared community-summary builder for Korea Invest Insights distribution.

Botmadang and Valley summary-mode posts should use the same community-facing
text. This module generates that text once per slug, caches it locally, and lets
each channel add only channel-specific affordances such as Valley cashtags.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any


DEFAULT_REPO_ROOT = Path.home() / "korea-invest-insights"
DEFAULT_CACHE_PATH = (
    Path.home()
    / ".local"
    / "share"
    / "korea-invest-insights"
    / "community_summary_cache.json"
)
BASE_URL_BLOG = "https://koreainvestinsights.com"
MIN_LEN = 600


REWRITE_PROMPT = """당신은 한국 주식시장 전문 AI 에이전트 '한국투자인사이트'입니다.
아래 한국어 블로그 포스트를 '봇마당 금융마당' 커뮤니티용 짧은 글로 리라이트하세요.

**발행 기준일: {date_str}** — 제목과 본문의 날짜 표현은 이 날짜를 기준으로 하세요.
원문에 다른 날짜(과거 지표 기준일 등)가 언급될 수 있지만, 포스트가 대표하는 날짜는 위입니다.

요구사항:
- 800~1500자 사이 한국어 본문
- 톤: 1인칭, 구어체("~에요", "~습니다" 혼용), 투자자 친구에게 인사이트 공유하듯
- 구조: (1) 팩트 한 줄 훅, (2) 남들이 놓친 앵글 1~2개 (숫자 근거 포함), (3) 내가 보는 시나리오/포지션, (4) 맨 마지막에 블로그 링크
- 과장·클릭베이트·이모지 남용 금지. 단, 숫자/데이터는 가능하면 그대로 인용
- 블로그 링크는 반드시 포함: {url}
- 마지막 한 줄은 커뮤니티에 의견을 묻는 질문으로 마무리

출력 형식(반드시 아래 두 태그 블록만 사용, 설명·코드블록·전후 텍스트 금지):

<TITLE>
여기에 제목만 한 줄로 (30~80자, 한국어)
</TITLE>
<CONTENT>
여기에 본문만 (800~1500자, 마크다운/줄바꿈 자유롭게 사용 가능)
</CONTENT>

---원문 제목---
{orig_title}

---원문 본문---
{orig_body}
"""

TITLE_RE = re.compile(r"<TITLE>\s*(.+?)\s*</TITLE>", re.DOTALL)
CONTENT_RE = re.compile(r"<CONTENT>\s*(.+?)\s*</CONTENT>", re.DOTALL)


def split_front_matter(raw: str) -> tuple[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.DOTALL)
    if not match:
        return "", raw.strip()
    return match.group(1), match.group(2).strip()


def frontmatter_value(frontmatter: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*\"?(.+?)\"?\s*$", frontmatter, re.MULTILINE)
    return match.group(1).strip().strip('"') if match else ""


def read_ko_post(slug: str, repo_root: Path = DEFAULT_REPO_ROOT) -> dict[str, Any] | None:
    path = repo_root / "content" / "post" / slug / "index.ko.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    frontmatter, body = split_front_matter(text)
    title = frontmatter_value(frontmatter, "title") or slug
    date_str = (frontmatter_value(frontmatter, "date") or "")[:10]
    return {
        "slug": slug,
        "path": str(path),
        "fingerprint": source_fingerprint(path),
        "title": title,
        "body": body,
        "url": f"{BASE_URL_BLOG}/ko/post/{slug}/",
        "date_str": date_str,
    }


def source_fingerprint(path: Path) -> str:
    stat = path.stat()
    return f"{stat.st_size}:{stat.st_mtime_ns}"


def load_cache(path: Path = DEFAULT_CACHE_PATH) -> dict[str, Any]:
    path = path.expanduser()
    if not path.exists():
        return {"posts": {}}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"posts": {}}


def save_cache(cache: dict[str, Any], path: Path = DEFAULT_CACHE_PATH) -> None:
    path = path.expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cache, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass


def claude_env() -> dict[str, str]:
    env = os.environ.copy()
    fnm_bin = str(Path.home() / ".local/share/fnm/aliases/default/bin")
    env["PATH"] = f"{fnm_bin}:{env.get('PATH', '')}"
    if "CLAUDE_CODE_OAUTH_TOKEN" not in env:
        zshrc = Path.home() / ".zshrc"
        if zshrc.exists():
            for line in zshrc.read_text(encoding="utf-8", errors="ignore").splitlines():
                line = line.strip()
                if line.startswith("export CLAUDE_CODE_OAUTH_TOKEN="):
                    env["CLAUDE_CODE_OAUTH_TOKEN"] = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
    return env


def ask_claude_for_summary(title: str, body: str, url: str, date_str: str, timeout: int = 180) -> dict[str, str] | None:
    claude_bin = Path.home() / ".local/share/fnm/aliases/default/bin/claude"
    if not claude_bin.exists():
        return None
    prompt = REWRITE_PROMPT.format(
        orig_title=title,
        orig_body=body[:8000],
        url=url,
        date_str=date_str or "최근",
    )
    try:
        proc = subprocess.run(
            [str(claude_bin), "--model", "sonnet", "-p", prompt],
            capture_output=True,
            text=True,
            env=claude_env(),
            timeout=timeout,
            check=False,
        )
    except (subprocess.TimeoutExpired, OSError):
        return None
    if proc.returncode != 0:
        return None
    title_match = TITLE_RE.search(proc.stdout.strip())
    content_match = CONTENT_RE.search(proc.stdout.strip())
    if not title_match or not content_match:
        return None
    parsed = {
        "title": title_match.group(1).strip(),
        "content": content_match.group(1).strip(),
    }
    if not parsed["title"] or not parsed["content"]:
        return None
    return parsed


def strip_markdown(line: str) -> str:
    line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
    line = re.sub(r"\*\*([^*]+)\*\*", r"\1", line)
    line = re.sub(r"`([^`]+)`", r"\1", line)
    return line.strip(" -*_`")


def fallback_summary(title: str, body: str, url: str) -> dict[str, str]:
    picked: list[str] = []
    in_summary = False
    for raw_line in body.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        heading = line.lstrip("#").strip().lower()
        if heading in {"핵심 요약", "tl;dr"}:
            in_summary = True
            continue
        if in_summary and line.startswith("## "):
            break
        if in_summary and (line.startswith(("-", "*")) or not line.startswith("|")):
            picked.append(strip_markdown(line))
        if len(picked) >= 4:
            break

    if not picked:
        paragraphs = [strip_markdown(line) for line in body.splitlines() if line.strip() and not line.startswith("#")]
        picked = paragraphs[:3]

    content_lines = [
        f"{title}",
        "",
        "이번 글에서 제가 본 핵심은 아래 세 가지입니다.",
        "",
    ]
    content_lines.extend(f"- {item}" for item in picked if item)
    content_lines.extend(
        [
            "",
            f"자세한 분석: {url}",
            "",
            "여러분은 이 흐름을 어떻게 보고 계신가요?",
        ]
    )
    return {
        "title": title[:80],
        "content": "\n".join(content_lines).strip(),
    }


def ensure_url(content: str, url: str) -> str:
    if url in content:
        return content.strip()
    return content.rstrip() + f"\n\n자세한 분석: {url}"


def truthy(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "y", "on"}


def generate_botmadang_summary(
    slug: str,
    repo_root: Path | str = DEFAULT_REPO_ROOT,
    cache_path: Path | str = DEFAULT_CACHE_PATH,
    use_cache: bool = True,
    allow_generate: bool = True,
) -> dict[str, Any] | None:
    repo_root = Path(repo_root).expanduser()
    cache_path = Path(cache_path).expanduser()
    post = read_ko_post(slug, repo_root)
    if not post:
        return None

    cache = load_cache(cache_path)
    cached = cache.get("posts", {}).get(slug)
    if use_cache and cached and cached.get("fingerprint") == post["fingerprint"]:
        return {**cached, "source": "cache"}

    generated = None
    source = "fallback"
    allow_generate = allow_generate and not truthy(os.environ.get("KII_COMMUNITY_SUMMARY_NO_GENERATE"))
    if allow_generate:
        generated = ask_claude_for_summary(post["title"], post["body"], post["url"], post["date_str"])
        if generated:
            source = "claude"
    if not generated:
        generated = fallback_summary(post["title"], post["body"], post["url"])

    result = {
        "slug": slug,
        "fingerprint": post["fingerprint"],
        "title": generated["title"].strip(),
        "content": ensure_url(generated["content"].strip(), post["url"]),
        "url": post["url"],
        "date_str": post["date_str"],
        "source": source,
    }

    if source == "claude":
        cache.setdefault("posts", {})[slug] = {k: v for k, v in result.items() if k != "source"}
        save_cache(cache, cache_path)

    return result


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    parser.add_argument("--repo-root", default=str(DEFAULT_REPO_ROOT))
    parser.add_argument("--no-cache", action="store_true")
    parser.add_argument("--no-generate", action="store_true")
    args = parser.parse_args()

    result = generate_botmadang_summary(
        args.slug,
        repo_root=args.repo_root,
        use_cache=not args.no_cache,
        allow_generate=not args.no_generate,
    )
    if not result:
        print(json.dumps({"success": False, "error": "post not found"}, ensure_ascii=False))
        return 1
    print(json.dumps({"success": True, **result}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
