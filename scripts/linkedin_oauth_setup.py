#!/usr/bin/env python3
"""One-time LinkedIn OAuth setup for the `linkedin` distribution channel.

Run this once (and again whenever the access token expires) to authorize the
blog to post to YOUR personal LinkedIn profile. You authorize in your own
browser — this script never sees your LinkedIn password.

Prerequisites (do these on developer.linkedin.com yourself):
  1. Create a LinkedIn app.
  2. Add the products "Share on LinkedIn" and
     "Sign In with LinkedIn using OpenID Connect".
  3. Under Auth, add this redirect URL:  http://localhost:8473/callback
  4. Copy the app's Client ID and Client Secret.

Then put the app credentials in the local secrets file (NOT committed):
    ~/.config/korea-invest-insights/linkedin.env
with at least:
    LINKEDIN_CLIENT_ID=...
    LINKEDIN_CLIENT_SECRET=...

Run:
    python3 scripts/linkedin_oauth_setup.py

It opens a browser, you click "Allow", and it writes the access token,
refresh token, expiry and your member URN back into linkedin.env.

Tokens: the member access token is valid ~60 days. A refresh token (if your app
is approved for it) lets the notify script renew silently for ~1 year; otherwise
re-run this script when posting starts to fail with an auth error.
"""

from __future__ import annotations

import http.server
import json
import secrets
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from pathlib import Path

from linkedin_notify import ENV_PATH, read_env, write_env  # type: ignore

REDIRECT_URI = "http://localhost:8473/callback"
AUTH_URL = "https://www.linkedin.com/oauth/v2/authorization"
TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"
USERINFO_URL = "https://api.linkedin.com/v2/userinfo"
SCOPE = "openid profile w_member_social"

_received: dict[str, str] = {}


class _Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path != "/callback":
            self.send_response(404)
            self.end_headers()
            return
        params = urllib.parse.parse_qs(parsed.query)
        _received["code"] = params.get("code", [""])[0]
        _received["state"] = params.get("state", [""])[0]
        _received["error"] = params.get("error", [""])[0]
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        msg = "LinkedIn 인증 완료. 이 창을 닫고 터미널로 돌아가세요." if not _received["error"] else f"오류: {_received['error']}"
        self.wfile.write(f"<html><body style='font-family:sans-serif'><h3>{msg}</h3></body></html>".encode("utf-8"))

    def log_message(self, *args) -> None:  # silence
        return


def _exchange_code(code: str, client_id: str, client_secret: str) -> dict:
    data = urllib.parse.urlencode(
        {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
            "client_id": client_id,
            "client_secret": client_secret,
        }
    ).encode("utf-8")
    req = urllib.request.Request(TOKEN_URL, data=data, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _fetch_member_urn(access_token: str) -> str:
    req = urllib.request.Request(USERINFO_URL)
    req.add_header("Authorization", f"Bearer {access_token}")
    with urllib.request.urlopen(req, timeout=20) as resp:
        info = json.loads(resp.read().decode("utf-8"))
    sub = info.get("sub", "")
    return f"urn:li:person:{sub}" if sub else ""


def main() -> int:
    env = read_env()
    client_id = env.get("LINKEDIN_CLIENT_ID")
    client_secret = env.get("LINKEDIN_CLIENT_SECRET")
    if not client_id or not client_secret:
        print(
            "LINKEDIN_CLIENT_ID / LINKEDIN_CLIENT_SECRET가 없습니다.\n"
            f"먼저 {ENV_PATH} 에 아래 두 줄을 넣어주세요:\n"
            "  LINKEDIN_CLIENT_ID=...\n"
            "  LINKEDIN_CLIENT_SECRET=...\n"
            "(developer.linkedin.com 앱의 Client ID/Secret)"
        )
        return 1

    state = secrets.token_urlsafe(16)
    auth_query = urllib.parse.urlencode(
        {
            "response_type": "code",
            "client_id": client_id,
            "redirect_uri": REDIRECT_URI,
            "scope": SCOPE,
            "state": state,
        }
    )
    auth_url = f"{AUTH_URL}?{auth_query}"

    server = http.server.HTTPServer(("127.0.0.1", 8473), _Handler)
    thread = threading.Thread(target=server.handle_request, daemon=True)
    thread.start()

    print("브라우저에서 LinkedIn 인증을 진행하세요. 자동으로 안 열리면 아래 URL을 직접 여세요:\n")
    print(auth_url, "\n")
    try:
        webbrowser.open(auth_url)
    except Exception:
        pass

    # Wait for the callback (up to 3 minutes).
    for _ in range(180):
        if _received.get("code") or _received.get("error"):
            break
        time.sleep(1)
    server.server_close()

    if _received.get("error"):
        print(f"인증 오류: {_received['error']}")
        return 1
    if _received.get("state") != state:
        print("state 불일치 — 보안상 중단했습니다. 다시 시도하세요.")
        return 1
    code = _received.get("code")
    if not code:
        print("인증 코드를 받지 못했습니다(시간 초과).")
        return 1

    try:
        token_payload = _exchange_code(code, client_id, client_secret)
    except urllib.error.HTTPError as exc:
        print(f"토큰 교환 실패: HTTP {exc.code}: {exc.read().decode('utf-8','ignore')[:300]}")
        return 1

    access_token = token_payload.get("access_token")
    if not access_token:
        print(f"access_token이 없습니다: {token_payload}")
        return 1

    member_urn = _fetch_member_urn(access_token)
    if not member_urn:
        print("멤버 URN(sub)을 가져오지 못했습니다. 'Sign In with LinkedIn using OpenID Connect' 제품이 활성화됐는지 확인하세요.")
        return 1

    env["LINKEDIN_ACCESS_TOKEN"] = access_token
    env["LINKEDIN_MEMBER_URN"] = member_urn
    if token_payload.get("refresh_token"):
        env["LINKEDIN_REFRESH_TOKEN"] = token_payload["refresh_token"]
    if token_payload.get("expires_in"):
        env["LINKEDIN_TOKEN_EXPIRES_AT"] = str(int(time.time()) + int(token_payload["expires_in"]))
    write_env(env)

    expires_days = round(int(token_payload.get("expires_in", 0)) / 86400, 1)
    print("\n✅ LinkedIn 설정 완료.")
    print(f"  member URN: {member_urn}")
    print(f"  토큰 만료: 약 {expires_days}일 후" + ("  (refresh token 저장됨 — 자동 갱신)" if token_payload.get("refresh_token") else "  (refresh token 없음 — 만료 시 이 스크립트 재실행)"))
    print(f"  저장 위치: {ENV_PATH} (로컬 전용, 커밋 금지)")
    print("\n이제 배포 시 LinkedIn 채널이 자동 발행됩니다. 단건 테스트:")
    print("  scripts/post_publish_distribution.py --slug <slug> --channels linkedin --max-posts 1")
    return 0


if __name__ == "__main__":
    sys.exit(main())
