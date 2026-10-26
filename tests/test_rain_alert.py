import sys
import unittest
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import rain_alert as ra  # noqa: E402


class KmaTests(unittest.TestCase):
    def test_grid_seoul_city_hall(self):
        # 기상청 격자 목록: 서울특별시 중구 = (60, 127)
        self.assertEqual(ra.latlon_to_kma_grid(37.5665, 126.9780), (60, 127))

    def test_parse_pcp(self):
        self.assertEqual(ra.parse_kma_pcp("강수없음"), 0.0)
        self.assertEqual(ra.parse_kma_pcp("1mm 미만"), 0.5)
        self.assertEqual(ra.parse_kma_pcp("1.0mm 미만"), 0.5)
        self.assertEqual(ra.parse_kma_pcp("6.0mm"), 6.0)
        self.assertEqual(ra.parse_kma_pcp("30.0~50.0mm"), 30.0)
        self.assertEqual(ra.parse_kma_pcp("50.0mm 이상"), 50.0)

    def test_base_time(self):
        at = lambda h, m: datetime(2026, 10, 26, h, m, tzinfo=ra.KST)
        self.assertEqual(ra.kma_base_time(at(9, 0)), at(8, 0))
        self.assertEqual(ra.kma_base_time(at(8, 10)), at(5, 0))
        self.assertEqual(ra.kma_base_time(at(1, 0)).day, 25)
        self.assertEqual(ra.kma_base_time(at(1, 0)).hour, 23)


class EvaluateTests(unittest.TestCase):
    def test_hits_and_missing(self):
        sources = [
            {"name": "A", "short": "A", "daily": {"2026-10-29": 25.0}, "error": None},
            {"name": "B", "short": "B", "daily": {"2026-10-29": 19.9}, "error": None},
            {"name": "C", "short": "C", "daily": {}, "error": "fail"},
        ]
        days = ra.evaluate(sources, date(2026, 10, 26), threshold=20)
        self.assertEqual(len(days), 7)
        d = days[3]
        self.assertEqual(d["date"], "2026-10-29")
        self.assertEqual(d["available"], 2)
        self.assertEqual(d["hits"], {"A": 25.0})
        msg = ra.build_message(sources, days, datetime(2026, 10, 26, 9, 0, tzinfo=ra.KST))
        self.assertIn("10/29(목)", msg)
        self.assertIn("2곳 중 <b>1곳</b>", msg)
        self.assertIn("응답 실패", msg)


if __name__ == "__main__":
    unittest.main()
