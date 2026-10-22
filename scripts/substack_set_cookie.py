#!/usr/bin/env python3
"""Refresh the Substack session cookie used by the unattended publisher.

The runtime publisher (substack_publisher.py) authenticates with the connect.sid
session cookie stored in the Gyeokja workspace config. That cookie is HttpOnly, so no
script can read it from the browser. The user copies it once from DevTools
(Application -> Cookies -> https://substack.com -> connect.sid or substack.sid):

  python3 scripts/substack_set_cookie.py --clipboard     # value is on the clipboard
  python3 scripts/substack_set_cookie.py                 # hidden prompt

The value is never printed or logged. It is written only after substack_gate.gate_status
reports "ok": a side-effect-free probe that Substack answers with 403 reauthentication_required
when the session must sign in again, and 404 when publishing is allowed. Reads (profile,
drafts list) pass even for a session that cannot publish, so they are not used. The old
value stays untouched when the check fails. File mode is 600.

  python3 scripts/substack_set_cookie.py --check         # test the stored cookie only

Copy the cookie right after a fresh sign-in. On 2026-10-22 the cookie saved in April
returned reauthentication_required while a fresh browser session passed. How long a fresh
session keeps passing is not known; if the publisher logs that error again, sign in again.

Interactive publishing does not need this: a logged-in browser pane can publish through
scripts/substack_pane_push.js. See memory note substack-publish-workflow.
"""
from __future__ import annotations

import argparse
import getpass
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from substack_gate import gate_status  # noqa: E402

CONFIG = Path.home() / "ThesisOS/repos/runtime/agents/gyeokja/workspace/data/substack_config.json"


def clean(raw: str) -> str:
    v = raw.strip().strip('"').strip("'")
    v = re.sub(r"^(connect\.sid|substack\.sid)=", "", v)
    return v.split(";")[0].strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--clipboard", action="store_true", help="read the cookie value from the clipboard (pbpaste)")
    ap.add_argument("--check", action="store_true", help="test the stored cookie and exit")
    ap.add_argument("--config", type=Path, default=CONFIG)
    a = ap.parse_args()

    cfg = json.loads(a.config.read_text(encoding="utf-8"))
    sub = cfg.get("subdomain", "")
    if not sub:
        print("config has no subdomain", file=sys.stderr)
        return 2
    if a.check:
        g = gate_status(sub, cfg.get("connect_sid", ""))
        print(f"stored cookie: {g}")
        return 0 if g == "ok" else 1
    raw = (subprocess.run(["pbpaste"], capture_output=True, text=True).stdout
           if a.clipboard else getpass.getpass("connect.sid value (hidden): "))
    value = clean(raw)
    if len(value) < 40:
        print("value too short to be a session cookie; nothing written", file=sys.stderr)
        return 2

    g = gate_status(sub, value)
    print(f"publish gate: {g}")
    if g != "ok":
        hint = {"reauth": "the session needs a fresh sign-in; sign in again, then copy the cookie",
                "invalid": "not a valid session cookie; copy connect.sid or substack.sid for substack.com"}.get(g, "network or unexpected response")
        print(f"config NOT changed: {hint}.", file=sys.stderr)
        return 1

    cfg["connect_sid"] = value
    fd, tmp = tempfile.mkstemp(dir=str(a.config.parent), suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.chmod(tmp, 0o600)
    os.replace(tmp, a.config)
    print(f"config updated: {a.config} (mode 600)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
