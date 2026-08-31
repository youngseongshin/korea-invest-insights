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

    def test_process_heading_warns(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "index.ko.md"
            path.write_text(
                "---\ntitle: 테스트\n---\n\n## 비교 분석\n\n두 회사의 영업이익률은 각각 12%와 8%입니다.\n",
                encoding="utf-8",
            )
            errors, warnings = iter_diagnostics(path)
            self.assertEqual(errors, 0)
            self.assertGreaterEqual(warnings, 1)

    def test_dense_paragraph_warns(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "index.ko.md"
            long_paragraph = "매출은 늘었지만 현금흐름은 아직 약합니다. " * 30
            path.write_text(
                f"---\ntitle: 테스트\n---\n\n{long_paragraph}\n",
                encoding="utf-8",
            )
            errors, warnings = iter_diagnostics(path)
            self.assertEqual(errors, 0)
            self.assertGreaterEqual(warnings, 1)

    def test_long_sentence_warns(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "index.ko.md"
            long_sentence = "매출 증가와 고객 다변화가 확인됐지만 " + ("현금흐름과 수익성 검증이 더 필요하고 " * 12) + "아직 결론은 이릅니다."
            path.write_text(
                f"---\ntitle: 테스트\n---\n\n{long_sentence}\n",
                encoding="utf-8",
            )
            errors, warnings = iter_diagnostics(path)
            self.assertEqual(errors, 0)
            self.assertGreaterEqual(warnings, 1)

    def test_markdown_structures_do_not_trigger_density_warning(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "index.ko.md"
            table_rows = "\n".join(f"| 항목 {i} | {i} |" for i in range(80))
            path.write_text(
                f"---\ntitle: 테스트\n---\n\n| 항목 | 값 |\n|---|---|\n{table_rows}\n",
                encoding="utf-8",
            )
            errors, warnings = iter_diagnostics(path)
            self.assertEqual(errors, 0)
            self.assertEqual(warnings, 0)


if __name__ == "__main__":
    unittest.main()
