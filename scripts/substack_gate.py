#!/usr/bin/env python3
"""Side-effect-free check that a Substack session cookie may publish.

Substack answers a publish call with 403 reauthentication_required when the session
needs a fresh sign-in, and it does so before it looks up the post. Probing a draft id
that cannot exist therefore separates the cases without creating or changing anything:

  ok       404 Post not found        the gate passed; publishing would be allowed
  reauth   403 reauthentication_required   sign in again, then refresh the cookie
  invalid  401 / other 403           the cookie is not a valid session
  error    network or unexpected status

Observed 2026-10-22: the cookie saved in April returned reauth, a fresh browser
session returned ok. Read calls (profile, drafts list) pass in both cases, so they say
nothing about publishing.
"""
from __future__ import annotations

import json
import urllib.error
import urllib.request

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
PROBE_DRAFT_ID = 2147483000  # no such draft; the request is rejected before any lookup side effect


def gate_status(subdomain: str, cookie: str) -> str:
    req = urllib.request.Request(
        f"https://{subdomain}.substack.com/api/v1/drafts/{PROBE_DRAFT_ID}/publish",
        data=json.dumps({"send": False, "type": "new"}).encode(),
        headers={"Content-Type": "application/json", "User-Agent": UA,
                 "Cookie": f"connect.sid={cookie}; substack.sid={cookie}"},
        method="POST")
    try:
        urllib.request.urlopen(req, timeout=20)
        return "error:unexpected-200"
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace") if e.fp else ""
        if e.code == 404:
            return "ok"
        if e.code == 403 and "reauthentication_required" in body:
            return "reauth"
        if e.code in (401, 403):
            return "invalid"
        return f"error:{e.code}"
    except OSError as e:
        return f"error:{type(e).__name__}"


if __name__ == "__main__":
    import sys
    from pathlib import Path
    cfg = json.loads((Path.home() / "ThesisOS/repos/runtime/agents/gyeokja/workspace/data/substack_config.json")
                     .read_text(encoding="utf-8"))
    print(gate_status(cfg["subdomain"], cfg["connect_sid"]))
