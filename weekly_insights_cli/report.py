"""读一周记录，汇总完成率、趋势、建议。内置示例。"""
from __future__ import annotations
import csv, json
from dataclasses import dataclass

SAMPLE_RECORDS = [
    {"date": "2026-09-28", "task": "写周报", "done": True},
    {"date": "2026-09-28", "task": "跑步", "done": False},
    {"date": "2026-09-29", "task": "写周报", "done": True},
    {"date": "2026-09-29", "task": "读书", "done": True},
    {"date": "2026-09-30", "task": "跑步", "done": True},
    {"date": "2026-10-01", "task": "读书", "done": False},
    {"date": "2026-10-02", "task": "写周报", "done": True},
    {"date": "2026-10-03", "task": "跑步", "done": True},
]


@dataclass
class Summary:
    total: int
    done: int
    rate: float
    by_task: dict


def load_records(path):
    if path.endswith(".csv"):
        with open(path, encoding="utf-8") as f: return list(csv.DictReader(f))
    with open(path, encoding="utf-8") as f: return json.load(f)


def summarize(records):
    total = len(records)
    done = sum(1 for r in records if str(r.get("done")).lower() in ("1", "true", "yes"))
    by_task = {}
    for r in records:
        t = r.get("task", "?")
        d = by_task.setdefault(t, {"done": 0, "total": 0})
        d["total"] += 1
        if str(r.get("done")).lower() in ("1", "true", "yes"): d["done"] += 1
    rate = round(done/total, 2) if total else 0.0
    return Summary(total=total, done=done, rate=rate, by_task=by_task)


def build_report(records):
    s = summarize(records)
    lines = [f"本周共 {s.total} 条记录，完成 {s.done} 条，完成率 {int(s.rate*100)}%。", ""]
    lines.append("按任务：")
    for t, d in s.by_task.items(): lines.append(f"  - {t}: {d['done']}/{d['total']}")
    weak = [t for t, d in s.by_task.items() if d["done"]/max(1,d["total"]) < 0.5]
    lines.append("")
    lines.append(f"建议关注低完成项：{', '.join(weak)}。" if weak else "整体执行良好，继续保持。")
    return "\n".join(lines)
