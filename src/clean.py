# src/clean.py
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # trim strings
    for col in out.select_dtypes(include=["object"]).columns:
        out[col] = out[col].astype(str).str.strip()

    # remove exact duplicate rows
    out = out.drop_duplicates()

    # basic type coercions
    out["age"] = pd.to_numeric(out["age"], errors="coerce")
    out["income"] = pd.to_numeric(out["income"], errors="coerce")
    out["signup_date"] = pd.to_datetime(out["signup_date"], errors="coerce").dt.date

    return out
