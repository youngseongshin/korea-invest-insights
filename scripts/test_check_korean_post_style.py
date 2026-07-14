from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from check_korean_post_style import iter_diagnostics


class KoreanPostStyleTest(unittest.TestCase):
    def test_scaffolding_blocks_blog_post(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "index.ko.md"
            path.write_text(
                "---\ntitle: 테스트\n---\n\n이 글에서는 시장을 살펴봅니다. 결론적으로 가격이 비쌉니다.\n",
                encoding="utf-8",
            )
            errors, _ = iter_diagnostics(path)
            self.assertGreaterEqual(errors, 2)

    def test_fact_first_post_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "index.ko.md"
            path.write_text(
                "---\ntitle: 테스트\n---\n\n2026년 영업이익은 100억 원으로 전년보다 25% 늘었다.\n",
                encoding="utf-8",
            )
            errors, _ = iter_diagnostics(path)
            self.assertEqual(errors, 0)


if __name__ == "__main__":
    unittest.main()
