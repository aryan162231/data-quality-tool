# src/main.py
import argparse
from src.io_utils import read_table, write_csv
from src.rules import RULES
from src.validate import run_all_checks
from src.clean import clean_data
from src.report import build_html_report
import pandas as pd

def combine_issue_rows(results: dict) -> pd.DataFrame:
    frames = []
    for k, v in results.items():
        if k == "fatal":
            continue
        if isinstance(v, pd.DataFrame) and not v.empty:
            temp = v.copy()
            temp["issue_type"] = k
            frames.append(temp)
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)

def main():
    parser = argparse.ArgumentParser(description="Data Validation & Cleaning Tool")
    parser.add_argument("--input", required=True, help="Path to input CSV or XLSX")
    parser.add_argument("--cleaned_out", default="data/processed/cleaned_output.csv")
    parser.add_argument("--issues_out", default="reports/issues.csv")
    parser.add_argument("--report_out", default="reports/validation_report.html")
    args = parser.parse_args()

    df_raw = read_table(args.input)
    df_clean = clean_data(df_raw)

    results = run_all_checks(df_clean, RULES)

    # Report
    build_html_report(results, total_rows=len(df_clean), out_path=args.report_out)

    if results.get("fatal"):
        print("Fatal issues found. See report:", args.report_out)
        return

    # Write outputs
    issues = combine_issue_rows(results)
    write_csv(df_clean, args.cleaned_out)
    if not issues.empty:
        write_csv(issues, args.issues_out)

    print("Done.")
    print("Cleaned file:", args.cleaned_out)
    print("Issues file:", args.issues_out if not issues.empty else "(none)")
    print("Report:", args.report_out)

if __name__ == "__main__":
    main()
