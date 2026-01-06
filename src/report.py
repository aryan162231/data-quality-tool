# src/report.py
from pathlib import Path
import pandas as pd

def _count_rows(df: pd.DataFrame) -> int:
    return 0 if df is None else int(df.shape[0])

def build_html_report(results: dict, total_rows: int, out_path: str) -> str:
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)

    sections = []
    sections.append(f"<h1>Data Validation Report</h1>")
    sections.append(f"<p><b>Total rows processed:</b> {total_rows}</p>")

    if results.get("fatal"):
        sections.append("<h2>Fatal Issues</h2><ul>")
        for msg in results["fatal"]:
            sections.append(f"<li>{msg}</li>")
        sections.append("</ul>")
    else:
        sections.append("<h2>Checks Summary</h2><ul>")
        for k, v in results.items():
            if k == "fatal":
                continue
            if isinstance(v, pd.DataFrame):
                sections.append(f"<li><b>{k}:</b> {_count_rows(v)} rows</li>")
        sections.append("</ul>")

    html = "<html><body>" + "\n".join(sections) + "</body></html>"
    Path(out_path).write_text(html, encoding="utf-8")
    return out_path
