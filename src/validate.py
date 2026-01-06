# src/validate.py
import pandas as pd
from datetime import datetime

def validate_required_columns(df: pd.DataFrame, required_cols: list[str]) -> list[str]:
    missing = [c for c in required_cols if c not in df.columns]
    issues = []
    if missing:
        issues.append(f"Missing required columns: {missing}")
    return issues

def find_missing_values(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    # returns rows with missing values in any required col
    mask = df[cols].isna().any(axis=1)
    return df[mask].copy()

def find_duplicates(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    dup_mask = df.duplicated(subset=cols, keep=False)
    return df[dup_mask].copy()

def validate_allowed_values(df: pd.DataFrame, col: str, allowed: list[str]) -> pd.DataFrame:
    bad = df[~df[col].isin(allowed)].copy()
    return bad

def validate_range(df: pd.DataFrame, col: str, min_val: float, max_val: float) -> pd.DataFrame:
    # coerce to numeric, invalid becomes NaN
    vals = pd.to_numeric(df[col], errors="coerce")
    bad = df[(vals < min_val) | (vals > max_val) | vals.isna()].copy()
    return bad

def validate_date_not_future(df: pd.DataFrame, col: str) -> pd.DataFrame:
    parsed = pd.to_datetime(df[col], errors="coerce")
    today = pd.Timestamp(datetime.today().date())
    bad = df[(parsed.isna()) | (parsed > today)].copy()
    return bad

def run_all_checks(df: pd.DataFrame, rules: dict) -> dict:
    """
    Returns a dict of issues:
      {
        "fatal": [strings],
        "missing_values": df,
        "duplicates": df,
        "bad_province": df,
        "bad_age": df,
        "bad_income": df,
        "bad_signup_date": df
      }
    """
    results = {"fatal": []}

    required_cols = rules["required_columns"]
    results["fatal"].extend(validate_required_columns(df, required_cols))
    if results["fatal"]:
        return results  # stop early

    results["missing_values"] = find_missing_values(df, required_cols)
    results["duplicates"] = find_duplicates(df, rules.get("unique_columns", []))

    # allowed values
    for col, allowed in rules.get("allowed_values", {}).items():
        results[f"bad_{col}"] = validate_allowed_values(df, col, allowed)

    # ranges
    for col, spec in rules.get("ranges", {}).items():
        results[f"bad_{col}"] = validate_range(df, col, spec["min"], spec["max"])

    # dates
    results["bad_signup_date"] = validate_date_not_future(df, "signup_date")

    return results
