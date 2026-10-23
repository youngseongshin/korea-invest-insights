#!/usr/bin/env python3
"""Substack-first distribution and the browser publish receipt (M-20261023-25)."""

from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))

import post_publish_distribution as ppd  # noqa: E402
import substack_record_browser_publish as recorder  # noqa: E402

SLUG = "test-post-2026-10-23"
POST = "---\ntitle: \"Test post\"\ndescription: \"A test.\"\ndate: 2026-10-23T09:00:00+09:00\n---\nBody.\n"


class DistributionTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.repo = root / "repo"
        post_dir = self.repo / "content" / "post" / SLUG
        post_dir.mkdir(parents=True)
        for lang in ("ko", "en"):
            (post_dir / f"index.{lang}.md").write_text(POST, encoding="utf-8")
        data_dir = root / "data"
        patches = [
            mock.patch.object(ppd, "DEFAULT_DATA_DIR", data_dir),
            mock.patch.object(ppd, "LOCK_PATH", data_dir / "post_publish_distribution.lock"),
        ]
        for patch in patches:
            patch.start()
            self.addCleanup(patch.stop)
        self.addCleanup(self.tmp.cleanup)
        self.calls: list[str] = []
        stub = mock.patch.object(ppd, "run_telegram_for_post", side_effect=self._telegram)
        stub.start()
        self.addCleanup(stub.stop)

    def _telegram(self, post: dict, args) -> dict:
        self.calls.append(post["slug"])
        return {"status": "sent"}

    def run_main(self, *extra: str) -> tuple[int, list[dict]]:
        out = io.StringIO()
        argv = ["--repo-root", str(self.repo), "--slug", SLUG, "--no-require-live", "--channels", "substack,telegram", *extra]
        with redirect_stdout(out):
            code = ppd.main(argv)
        final = json.loads(out.getvalue().strip().splitlines()[-1])
        return code, final["channels"]

    def record(self, *extra: str) -> int:
        args = ["--repo-root", str(self.repo), "--slug", SLUG, "--no-live-check", *extra]
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            return recorder.main(args)


class SubstackFirstTest(DistributionTestCase):
    def test_default_channels_run_substack_first(self) -> None:
        self.assertEqual(ppd.DEFAULT_CHANNELS[0], "substack")
        self.assertEqual(ppd.CANDIDATE_CHANNEL_ORDER[0], "substack")
        self.assertEqual(ppd.REQUIRED_TRANSLATION_LANGS, ("ko", "en"))

    def test_missing_receipt_blocks_other_channels(self) -> None:
        code, channels = self.run_main()
        self.assertEqual(code, 1)
        self.assertEqual(channels[0], {"channel": "substack", "exitCode": 1})
        self.assertEqual(channels[1]["status"], "blocked_by_substack")
        self.assertEqual(self.calls, [])
        self.assertFalse(ppd.channel_log_path("substack").exists(), "pending must not be logged as sent")

    def test_receipt_lets_other_channels_run(self) -> None:
        self.assertEqual(self.record("--substack-url", "https://koreainvestinsights.substack.com/p/test-post",
                                     "--draft-id", "123", "--note-url", "https://substack.com/note/c-456"), 0)
        code, channels = self.run_main()
        self.assertEqual(code, 0)
        self.assertEqual([c["exitCode"] for c in channels], [0, 0])
        self.assertEqual(self.calls, [SLUG])

    def test_dry_run_reports_pending_without_blocking(self) -> None:
        code, channels = self.run_main("--dry-run")
        self.assertEqual(code, 0)
        self.assertEqual([c["channel"] for c in channels], ["substack", "telegram"])

    def test_leaving_substack_out_is_explicit(self) -> None:
        out = io.StringIO()
        with redirect_stdout(out):
            code = ppd.main(["--repo-root", str(self.repo), "--slug", SLUG, "--no-require-live", "--channels", "telegram"])
        self.assertEqual(code, 0)
        self.assertEqual(self.calls, [SLUG])


class RecorderTest(DistributionTestCase):
    def test_note_is_required_unless_an_exception_is_named(self) -> None:
        self.assertEqual(self.record("--substack-url", "https://koreainvestinsights.substack.com/p/x",
                                     "--draft-id", "1"), 2)
        self.assertEqual(self.record("--substack-url", "https://koreainvestinsights.substack.com/p/x",
                                     "--draft-id", "1", "--no-note", "user asked for no Note"), 0)
        entry = json.loads(ppd.channel_log_path("substack").read_text(encoding="utf-8"))["posts"]
        (key, value), = entry.items()
        self.assertEqual(key, f"https://koreainvestinsights.com/ko/post/{SLUG}/")
        self.assertEqual(value["mode"], "publish")
        self.assertEqual(value["response"]["no_note_reason"], "user asked for no Note")

    def test_rejects_wrong_urls_and_duplicates(self) -> None:
        self.assertEqual(self.record("--substack-url", "https://example.com/p/x", "--draft-id", "1",
                                     "--note-url", "https://substack.com/note/c-1"), 2)
        ok = ("--substack-url", "https://koreainvestinsights.substack.com/p/x", "--draft-id", "1",
              "--note-url", "https://substack.com/note/c-1")
        self.assertEqual(self.record(*ok), 0)
        self.assertEqual(self.record(*ok), 2)
        self.assertEqual(self.record(*ok, "--force"), 0)

    def test_check_reads_the_receipt(self) -> None:
        self.assertEqual(self.record("--check"), 1)
        self.record("--substack-url", "https://koreainvestinsights.substack.com/p/x", "--draft-id", "1",
                    "--note-url", "https://substack.com/note/c-1")
        self.assertEqual(self.record("--check"), 0)


if __name__ == "__main__":
    unittest.main()
