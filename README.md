# weekly-insights-cli

个人数据周报：读一周记录（JSON/CSV），汇总完成率、趋势、建议；内置示例。

## 快速开始
```python
from weekly_insights_cli import build_report, SAMPLE_RECORDS
print(build_report(SAMPLE_RECORDS))
```

## 运行测试
```bash
python -m unittest discover -s tests -v
```

## License
MIT © ljiang9
