#!/usr/bin/env python3
"""Refresh the Substack session cookie used by the unattended publisher.

The runtime publisher (substack_publisher.py) authenticates with the connect.sid
session cookie stored in the Gyeokja workspace config. That cookie is HttpOnly, so no
script can read it from the browser. The user copies it once from DevTools
(Application -> Cookies -> https://substack.com -> connect.sid or substack.sid):

  python3 scripts/substack_set_cookie.py --clipboard     # value is on the clipboard
  python3 scripts/substack_set_cookie.py                 # hidden prompt

The value is never printed or logged. It is written only after the Substack API accepts
it for reads, with file mode 600. The old value stays untouched when validation fails.

Limit of the check: it proves read access only. On 2026-10-10 the April cookie still passed
reads and draft creation while publish returned 403 reauthentication_required, so publishing
needs a recently authenticated session. Copy the cookie right after a fresh login, and
log in again when the publisher reports that error.

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
import urllib.error
import urllib.request
from pathlib import Path

CONFIG = Path.home() / "ThesisOS/repos/runtime/agents/gyeokja/workspace/data/substack_config.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


def status(url: str, cookie_header: str) -> int:
    req = urllib.request.Request(url, headers={"Cookie": cookie_header, "User-Agent": UA})
    try:
        return urllib.request.urlopen(req, timeout=20).status
    except urllib.error.HTTPError as e:
        return e.code
    except OSError:
        return -1


def clean(raw: str) -> str:
    v = raw.strip().strip('"').strip("'")
    v = re.sub(r"^(connect\.sid|substack\.sid)=", "", v)
    return v.split(";")[0].strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--clipboard", action="store_true", help="read the cookie value from the clipboard (pbpaste)")
    ap.add_argument("--config", type=Path, default=CONFIG)
    a = ap.parse_args()

    cfg = json.loads(a.config.read_text(encoding="utf-8"))
    sub = cfg.get("subdomain", "")
    if not sub:
        print("config has no subdomain", file=sys.stderr)
        return 2
    raw = (subprocess.run(["pbpaste"], capture_output=True, text=True).stdout
           if a.clipboard else getpass.getpass("connect.sid value (hidden): "))
    value = clean(raw)
    if len(value) < 40:
        print("value too short to be a session cookie; nothing written", file=sys.stderr)
        return 2

    # The publisher sends connect.sid; send both names so either cookie in the jar counts.
    header = f"connect.sid={value}; substack.sid={value}"
    profile = status("https://substack.com/api/v1/user/profile/self", header)
    pub = status(f"https://{sub}.substack.com/api/v1/drafts?limit=1", header)
    print(f"substack.com profile/self: HTTP {profile}")
    print(f"{sub}.substack.com drafts : HTTP {pub}")
    if profile != 200 or pub != 200:
        print("validation failed; config NOT changed. Re-copy the cookie right after logging in.", file=sys.stderr)
        return 1

    cfg["connect_sid"] = value
    fd, tmp = tempfile.mkstemp(dir=str(a.config.parent), suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.chmod(tmp, 0o600)
    os.replace(tmp, a.config)
    print(f"config updated: {a.config} (mode 600)")
    print("note: reads passed. Publishing still needs a recently authenticated session; "
          "on 403 reauthentication_required, log in again and rerun this.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
