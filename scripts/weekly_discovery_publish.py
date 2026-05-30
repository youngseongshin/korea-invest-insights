#!/usr/bin/env python3
"""Weekly Discovery → public blog publisher (transform + redaction gate; dry-run first).

Pipeline:
  격자 vault `{date}_weekly-discovery-review.md`
    → editorial transform: KEEP thematic discovery (§1 애널리스트 리포트 발굴 /
      §2 스크리너 발굴 / §3 리포트×스크리너 교집합); DROP portfolio-decision
      sections (§4 실전 편입 후보 / §5 소액 옵션 / §6 추격 주의 / §7 체크포인트).
    → redaction gate: HARD-BLOCK on positions/funding/holdings/vault-paths/PII/
      secrets (never publishable); SOFT-WARN on ambiguous trade verbs.
    → Hugo draft post (`content/post/<slug>/index.ko.md`, draft: true).

SAFETY (registry M-20260530-03; public scope = "종목명 OK, 포지션 차단"):
  - dry-run is the DEFAULT: nothing is written unless --write-draft.
  - A HARD gate violation blocks output (exit 2). Nothing is written.
  - draft: true means the distribution stage (post_publish_distribution.py) skips
    it — so even a written draft is never auto-distributed. Go-live = a human sets
    draft: false after review (or rerun with --publish once trusted).

Dependency-free (stdlib only), mirroring scripts of the ThesisOS redaction gate.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
# The private vault source path is NOT hardcoded here (this repo is public). It is
# read from $KII_DISCOVERY_BRIEFS_DIR or ~/.config/korea-invest-insights/discovery.env.
DISCOVERY_ENV = Path.home() / ".config" / "korea-invest-insights" / "discovery.env"


def briefs_dir() -> Path | None:
    env = os.environ.get("KII_DISCOVERY_BRIEFS_DIR")
    if env:
        return Path(env).expanduser()
    try:
        for line in DISCOVERY_ENV.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("KII_DISCOVERY_BRIEFS_DIR="):
                return Path(line.split("=", 1)[1].strip()).expanduser()
    except OSError:
        pass
    return None

# Section heading number → keep vs drop.
# §1 analyst reports + §2 screener lists are summaries of EXTERNAL data (tickers OK).
# §3 (교집합) onward interleaves 격자's OWN portfolio judgment — holdings, sizing,
# buy/sell, timing — so it is dropped. (Learned 2026-05-30: §3 leaked "이미 포트에 있고
# / 일부 현금화 후보 / 1~2% 파일럿 / 추격 금지 / 종가·RSI"; keep-list tightened to §1-2,
# unknown/unnumbered sections now also drop, and the gate was hardened below.)
KEEP_SECTIONS = {"1", "2"}

# HARD: true confidentiality leaks. Never legitimately in a public thematic post.
# THIS REPO IS PUBLIC — in-repo patterns are GENERIC only (Korean-finance position
# vocabulary + secret SHAPES, no real ids/names). Owner-specific PII, the internal
# vault taxonomy, and live ids load at runtime from an external gitignored file
# (~/.config/korea-invest-insights/redaction_patterns.txt) so they never enter git.
HARD_PATTERNS = {
    "포지션/사이징": re.compile(r"비중|오버\s?웨이트|언더\s?웨이트|풀\s?포지션|분할\s?(매수|매도)|파일럿|포지션\s*(사이|크기)|\d+\s*%\s*(이하|이상|내외)?\s*(파일럿|비중|편입)"),
    "재원/현금화": re.compile(r"재원|현금화|일부\s*현금|차익\s*실현|현금\s*\d+\s*%|현금\s*비중|실탄|비중\s*(축소|확대|조절)"),
    "보유/편입 공개": re.compile(r"이미\s*포트|포트(폴리오)?\s*에?\s*(있|편입|넣|담|실)|편입\s*후보|보유\s*(종목|중|비중|중인)|내\s*포트|우리\s*포트|들고\s*있"),
    "타이밍 판단": re.compile(r"추격\s*금지|눌림\s*(조건|대기|매수|시|에)|오버슛|신규\s*매수\s*후보|진입\s*금지"),
    "보유 디테일/계좌": re.compile(r"계좌|주문\s*번호|체결\s*(가|단가|내역)|평단가?|종가\s*[\d,]+\s*만\s*원|RSI\s*\d|수익률\s*[+\-]?\d"),
    "telegram bot token": re.compile(r"\b\d{8,10}:[A-Za-z0-9_-]{35}\b"),
    "api key": re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----"),
}

# Owner-specific PII / internal vault paths / live ids — kept OUT of this public repo.
EXTERNAL_PATTERNS_PATH = Path.home() / ".config" / "korea-invest-insights" / "redaction_patterns.txt"


def load_external_patterns() -> dict:
    """Compile one regex per non-comment line from the external (gitignored) file."""
    pats: dict = {}
    try:
        lines = EXTERNAL_PATTERNS_PATH.read_text(encoding="utf-8").splitlines()
    except OSError:
        return pats
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            pats[f"local-pii#{i}"] = re.compile(line, re.IGNORECASE)
        except re.error:
            continue
    return pats

# SOFT: ambiguous (analyst "매수 의견" is public; my "매수" is a position). Warn, not block.
SOFT_PATTERNS = {
    "매매 동사(검토 필요)": re.compile(r"익절|손절|축소|확대|리밸런싱|교체\s?매매|추격\s?매수|담(는다|아|을)|실(을|린|어)"),
}


def latest_brief(date: str | None) -> Path | None:
    base = briefs_dir()
    if not base or not base.is_dir():
        return None
    if date:
        hits = sorted(base.glob(f"{date}*weekly-discovery*.md"))
        return hits[0] if hits else None
    hits = sorted(base.glob("*weekly-discovery-review.md"))
    return hits[-1] if hits else None


def strip_front_matter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[text.find("\n", end + 1) + 1 :]
    return text


def split_sections(body: str) -> list[tuple[str, str]]:
    """Return [(heading_line, block_text)] split on '## ' headings."""
    parts: list[tuple[str, str]] = []
    cur_head, cur_lines = None, []
    for line in body.splitlines():
        if line.startswith("## "):
            if cur_head is not None:
                parts.append((cur_head, "\n".join(cur_lines)))
            cur_head, cur_lines = line, []
        else:
            cur_lines.append(line)
    if cur_head is not None:
        parts.append((cur_head, "\n".join(cur_lines)))
    return parts


def section_number(heading: str) -> str | None:
    m = re.match(r"##\s*(\d+)\.", heading)
    return m.group(1) if m else None


def transform(body: str) -> tuple[str, list[str]]:
    """Keep ONLY allow-listed external sections; drop everything else (default-deny).

    Return (public_md, dropped_headings). Unknown/unnumbered sections are dropped,
    not kept — a new portfolio-judgment section must never pass by default.
    """
    kept, dropped = [], []
    for heading, block in split_sections(body):
        num = section_number(heading)
        if num in KEEP_SECTIONS:
            kept.append(f"{heading}\n{block}".rstrip())
        else:
            dropped.append(heading.strip())
    return "\n\n".join(kept).strip(), dropped


def scan_gate(text: str) -> tuple[list[str], list[str]]:
    hard, soft = [], []
    patterns = {**HARD_PATTERNS, **load_external_patterns()}
    for label, rx in patterns.items():
        m = rx.search(text)
        if m:
            hard.append(f"{label}: …{m.group(0)}…")
    for label, rx in SOFT_PATTERNS.items():
        m = rx.search(text)
        if m:
            soft.append(f"{label}: …{m.group(0)}…")
    return hard, soft


def build_post(date: str, public_md: str, soft: list[str], publish: bool = False) -> str:
    # The DRAFT review banner is internal-only — it must never appear in a live
    # (draft:false) post. Published posts get a neutral one-line provenance note.
    if publish:
        notice = ""
    else:
        banner = (
            "> **DRAFT — 검토 필요.** 격자 주간 발굴 결산에서 비공개 포트폴리오 판단"
            "(리포트×스크리너 교집합·실전 편입 후보·비중·재원·소액 옵션·추격 주의·체크포인트)은 "
            "모두 제외하고, 외부 데이터 요약(§1 애널리스트 리포트 발굴 · §2 스크리너 발굴)만 추렸습니다. "
            "공개 전 반드시 사람이 검토하세요."
        )
        if soft:
            banner += "\n>\n> ⚠️ 검토 포인트(매매 동사 감지): " + "; ".join(soft)
        notice = banner + "\n\n"
    desc = "이번 주 애널리스트 리포트와 스크리너에서 반복 포착된 테마와 종목을 발굴 관점에서 정리한다. (비공개 포트폴리오 판단 제외)"
    return f"""---
title: "주간 발굴 결산 — {date} 테마·종목 디스커버리"
slug: "weekly-discovery-review-{date}"
date: {date}T19:30:00+09:00
description: "{desc}"
categories: ["Korea Market", "Discovery"]
tags:
  - "주간 발굴"
  - "애널리스트 리포트"
  - "스크리너"
  - "테마 디스커버리"
series: ["Weekly Discovery"]
draft: {"false" if publish else "true"}
---

{notice}{public_md}

---

_출처: 주간 발굴 결산(애널리스트 리포트 × 스크리너 발굴) 자동 추출. 비공개 포트폴리오 전략은 본 공개본에서 제외됨._
"""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Weekly discovery → public blog (transform+gate, dry-run first)")
    ap.add_argument("--date", help="YYYY-MM-DD of the brief (default: latest)")
    ap.add_argument("--write-draft", action="store_true", help="write the Hugo draft post (default: dry-run, write nothing)")
    ap.add_argument("--publish", action="store_true", help="set draft:false (go-live). Requires passing gate + explicit opt-in.")
    args = ap.parse_args(argv)

    if briefs_dir() is None:
        print(f"[skip] briefs source not configured — set $KII_DISCOVERY_BRIEFS_DIR or {DISCOVERY_ENV}.")
        return 0
    brief = latest_brief(args.date)
    if not brief or not brief.is_file():
        print(f"[skip] no weekly-discovery brief found (date={args.date or 'latest'}) — nothing to publish.")
        return 0
    date = re.match(r"(\d{4}-\d{2}-\d{2})", brief.name).group(1)
    print(f"[src] {brief}")

    body = strip_front_matter(brief.read_text(encoding="utf-8"))
    public_md, dropped = transform(body)
    print(f"[transform] dropped portfolio-decision sections: {dropped or '(none)'}")

    if not EXTERNAL_PATTERNS_PATH.is_file():
        print(f"[warn] external PII/path layer absent ({EXTERNAL_PATTERNS_PATH}); only generic patterns active.")

    hard, soft = scan_gate(public_md)
    if hard:
        print("[GATE: BLOCK] HARD confidentiality violations in public candidate:")
        for v in hard:
            print(f"   ✗ {v}")
        print("[result] nothing written. Fix the transform/source before publishing.")
        return 2
    print(f"[GATE: PASS] no HARD leaks. SOFT warnings: {soft or '(none)'}")

    post = build_post(date, public_md, soft, publish=args.publish)

    out_dir = REPO_ROOT / "content" / "post" / f"weekly-discovery-review-{date}"
    out_path = out_dir / "index.ko.md"
    if not args.write_draft and not args.publish:
        print(f"[dry-run] would write {out_path} ({len(post)} bytes, draft={'false' if args.publish else 'true'})")
        print("---- preview (first 1200 chars) ----")
        print(post[:1200])
        return 0

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path.write_text(post, encoding="utf-8")
    print(f"[ok] wrote {out_path} (draft={'false' if args.publish else 'true'})")
    if not args.publish:
        print("[next] review the draft, then set draft:false (or rerun --publish) to let post_publish_distribution pick it up.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
