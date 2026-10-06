"""weekly_insights_cli: 个人数据周报（读一周 JSON/CSV，汇总完成率/趋势/建议）。"""
from .report import load_records, summarize, build_report, SAMPLE_RECORDS

__all__ = ["load_records", "summarize", "build_report", "SAMPLE_RECORDS"]
__version__ = "0.1.0"
