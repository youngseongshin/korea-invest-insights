#!/usr/bin/env python3
"""Check Korean blog posts for recurring publishing style problems."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


SLOP_PHRASES = (
    "핵심은 이것이다",
    "이것이 바로",
    "놓치면 안 됩니다",
    "정확히는",
    "명확합니다",
    "한 문장으로 정리하면",
    "여기서 가설이 검증된다",
)

ENGLISH_HEAVY_TERMS = (
    "read-through",
    "optionality",
    "short thesis",
    "long thesis",
    "base case",
    "bullish",
    "bearish",
    "funding source",
)


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

        lowered = line.lower()
        for phrase in SLOP_PHRASES:
            if phrase in line:
                col = line.index(phrase) + 1
                warnings += 1
                print(
                    f"{path}:{line_no}:{col}: WARN: possible formulaic or AI-slop phrase "
                    f"'{phrase}'; rewrite if it reads unnaturally"
                )
        for term in ENGLISH_HEAVY_TERMS:
            if term in lowered:
                col = lowered.index(term) + 1
                warnings += 1
                print(
                    f"{path}:{line_no}:{col}: WARN: English-heavy term '{term}'; "
                    "keep only if standard for readers or explain once"
                )

    return hard_errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check Korean Korea Invest Insights markdown posts for style blockers."
    )
    parser.add_argument("paths", nargs="+", help="Korean markdown files to check")
    args = parser.parse_args()

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
