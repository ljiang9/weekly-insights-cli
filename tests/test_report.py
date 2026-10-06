import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from weekly_insights_cli.report import summarize, build_report, SAMPLE_RECORDS


class TestWeeklyInsights(unittest.TestCase):
    def test_rate(self):
        s = summarize(SAMPLE_RECORDS)
        self.assertEqual(s.total, 8); self.assertEqual(s.done, 6); self.assertEqual(s.rate, 0.75)
    def test_by_task(self):
        s = summarize(SAMPLE_RECORDS)
        self.assertEqual(s.by_task["跑步"]["total"], 3)
    def test_report_has_advice(self):
        self.assertIn("完成率", build_report(SAMPLE_RECORDS))
    def test_empty(self):
        self.assertIn("0", build_report([]))


if __name__ == "__main__": unittest.main()
