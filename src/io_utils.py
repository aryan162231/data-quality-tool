# src/io_utils.py
from pathlib import Path
import pandas as pd

def read_table(path: str) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    if p.suffix.lower() == ".csv":
        return pd.read_csv(p)
    elif p.suffix.lower() in [".xlsx", ".xls"]:
        return pd.read_excel(p)
    else:
        raise ValueError("Unsupported file type. Use .csv or .xlsx")

def write_csv(df: pd.DataFrame, path: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
