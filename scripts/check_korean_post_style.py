#!/usr/bin/env python3
"""Check Korean blog posts for recurring publishing style problems."""

from __future__ import annotations

import argparse
import importlib.util
import os
import re
import sys
from pathlib import Path


DEFAULT_SLOP_LINT = Path.home() / ".openclaw/skills/thesis-os-human-editor/scripts/slop_lint.py"
DEFAULT_EXTERNAL_PROOFREAD = Path.home() / ".openclaw/skills/thesis-os-human-editor/scripts/external_proofread.py"

ENGLISH_HEAVY_TERMS = {
    "read-through": "연결 영향",
    "optionality": "추가 성장 가능성 또는 선택권",
    "short thesis": "하락 논리",
    "long thesis": "상승 논리",
    "base case": "기본 시나리오",
    "bullish": "긍정적",
    "bearish": "부정적",
    "funding source": "자금 조달원",
    "choke point": "병목",
    "toll-road": "수수료형 사업 또는 통행료형 사업",
    "firm power": "안정적으로 공급할 수 있는 전력",
    "invalidation": "무효 조건",
    "macro failure mode": "거시 실패 조건",
    "micro failure mode": "기업별 실패 조건",
}

PROCESS_HEADING_RE = re.compile(
    r"^\s*#{1,6}\s*(?:\d+[.)]\s*)?"
    r"(?:총정리|정리|종합(?:\s*분석)?|비교\s*분석|상세\s*분석|살펴보기|"
    r"매칭\s*매트릭스|핵심\s*해석|최종\s*판단|투자\s*관점에서의\s*해석)\s*$",
    re.IGNORECASE,
)

MAX_PROSE_PARAGRAPH_CHARS = 500
MAX_PROSE_SENTENCE_CHARS = 190


def iter_prose_paragraphs(text: str):
    """Yield reader-facing prose paragraphs while skipping Markdown structures."""

    lines = text.splitlines()
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    in_fence = False
    paragraph: list[str] = []
    start_line = 0

    def flush():
        nonlocal paragraph, start_line
        if paragraph:
            yield start_line, " ".join(paragraph)
            paragraph = []
            start_line = 0

    for line_no, line in enumerate(lines, start=1):
        stripped = line.strip()

        if in_frontmatter:
            if line_no > 1 and stripped == "---":
                in_frontmatter = False
            continue

        if stripped.startswith("```"):
            yield from flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        is_structural = (
            not stripped
            or stripped.startswith(("#", "|", "<", ">", "- ", "* ", "+ ", "---", "{{"))
            or bool(re.match(r"^\d+[.)]\s+", stripped))
        )
        if is_structural:
            yield from flush()
            continue

        if not paragraph:
            start_line = line_no
        paragraph.append(stripped)

    yield from flush()


def visible_markdown_text(text: str) -> str:
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"[`*_~]", "", text).strip()


def load_slop_scanner():
    path = Path(os.environ.get("THESIS_OS_SLOP_LINT", DEFAULT_SLOP_LINT)).expanduser()
    if not path.exists():
        raise FileNotFoundError(path)
    spec = importlib.util.spec_from_file_location("thesis_os_blog_slop_lint", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load slop scanner: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def iter_diagnostics(path: Path) -> tuple[int, int]:
    hard_errors = 0
    warnings = 0
    in_fence = False

    text = path.read_text(encoding="utf-8")
    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if "—" in line:
            col = line.index("—") + 1
            hard_errors += 1
            print(
                f"{path}:{line_no}:{col}: ERROR: avoid em dash in Korean posts; "
                "rewrite with a comma, colon, parentheses, or a separate sentence"
            )

        if "**" in line:
            col = line.index("**") + 1
            hard_errors += 1
            print(
                f"{path}:{line_no}:{col}: ERROR: avoid raw Markdown bold '**' "
                "in Korean source; use <strong>...</strong> sparingly or remove emphasis"
            )

        if PROCESS_HEADING_RE.match(line):
            warnings += 1
            print(
                f"{path}:{line_no}:1: WARN: process-only heading; "
                "replace it with the section's actual answer or finding"
            )

        lowered = line.lower()
        for term, korean in ENGLISH_HEAVY_TERMS.items():
            if term in lowered:
                col = lowered.index(term) + 1
                warnings += 1
                print(
                    f"{path}:{line_no}:{col}: WARN: English-heavy term '{term}'; "
                    f"prefer '{korean}' or explain the term once"
                )

    for line_no, paragraph in iter_prose_paragraphs(text):
        visible = visible_markdown_text(paragraph)
        if len(visible) > MAX_PROSE_PARAGRAPH_CHARS:
            warnings += 1
            print(
                f"{path}:{line_no}:1: WARN: dense prose paragraph ({len(visible)} chars); "
                "keep one claim per paragraph and split changes in evidence or interpretation"
            )

        sentences = [part.strip() for part in re.split(r"(?<=[.!?])\s+", visible) if part.strip()]
        for sentence in sentences:
            if len(sentence) > MAX_PROSE_SENTENCE_CHARS:
                warnings += 1
                excerpt = sentence[:72] + ("..." if len(sentence) > 72 else "")
                print(
                    f"{path}:{line_no}:1: WARN: long sentence ({len(sentence)} chars): "
                    f"{excerpt} -> split the claim, evidence, and caveat into separate sentences"
                )

    try:
        slop = load_slop_scanner().scan_text(text, surface="blog")
    except Exception as exc:
        hard_errors += 1
        print(f"{path}: ERROR: Thesis OS slop scanner unavailable: {exc}")
        return hard_errors, warnings

    for finding in slop["findings"]:
        level = finding["severity"]
        if level == "FAIL":
            hard_errors += 1
        else:
            warnings += 1
        location = f":{finding['line']}:1" if finding["line"] else ""
        print(
            f"{path}{location}: {level}: {finding['category']}: "
            f"{finding['excerpt']} -> {finding['suggestion']}"
        )

    return hard_errors, warnings


def run_external_readthrough(path: Path) -> int:
    """Solar Human Proofreader read-through (Human Editor step 7). Non-blocking.

    Opt-in via --external-readthrough or THESIS_OS_EXTERNAL_PROOFREAD=1. The skill
    script refuses non-public surfaces, confidential paths, and non-Korean bodies,
    and never writes the file in read_through mode. Findings are printed for the
    author; they do not change the exit code of this gate. Returns the number of
    informational notes emitted (0 or 1).
    """
    import subprocess

    script = Path(os.environ.get("THESIS_OS_EXTERNAL_PROOFREAD_SCRIPT", str(DEFAULT_EXTERNAL_PROOFREAD)))
    if not script.is_file():
        print(f"{path}: INFO: external read-through skipped (script not found: {script})")
        return 0
    cmd = [sys.executable, str(script), "--file", str(path), "--surface", "blog",
           "--mode", "read_through", "--genre", "칼럼"]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    except (OSError, subprocess.SubprocessError) as exc:
        print(f"{path}: INFO: external read-through unavailable ({type(exc).__name__})")
        return 0
    if proc.returncode == 2:
        print(f"{path}: INFO: external read-through refused -> {proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else 'gate'}")
        return 0
    if proc.returncode != 0:
        print(f"{path}: INFO: external read-through error (exit {proc.returncode})")
        return 0
    print(f"{path}: INFO: external read-through (Solar Human Proofreader) -- review, not a blocker")
    print(proc.stdout.rstrip())
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check Korean Korea Invest Insights markdown posts for style blockers."
    )
    parser.add_argument("paths", nargs="+", help="Korean markdown files to check")
    parser.add_argument(
        "--external-readthrough",
        action="store_true",
        help="also run the Solar Human Proofreader read-through (non-blocking; "
        "or set THESIS_OS_EXTERNAL_PROOFREAD=1)",
    )
    args = parser.parse_args()
    external = args.external_readthrough or os.environ.get("THESIS_OS_EXTERNAL_PROOFREAD") == "1"

    total_errors = 0
    total_warnings = 0

    for raw_path in args.paths:
        path = Path(raw_path)
        if not path.exists():
            total_errors += 1
            print(f"{path}: ERROR: file does not exist")
            continue
        if path.suffix != ".md" or not path.name.endswith(".ko.md"):
            total_warnings += 1
            print(f"{path}: WARN: expected a Korean markdown file ending in .ko.md")

        errors, warnings = iter_diagnostics(path)
        total_errors += errors
        total_warnings += warnings
        if external and path.name.endswith(".ko.md") and errors == 0:
            run_external_readthrough(path)

    if total_errors:
        print(
            f"check_korean_post_style: failed with {total_errors} error(s) "
            f"and {total_warnings} warning(s)"
        )
        return 1

    print(f"check_korean_post_style: passed with {total_warnings} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
