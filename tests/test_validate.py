import pandas as pd
from src.validate import run_all_checks
from src.rules import RULES

def test_duplicates_detected():
    df = pd.DataFrame({
        "student_id": [1, 2, 2],
        "name": ["A", "B", "B"],
        "email": ["a@a.com", "b@b.com", "b@b.com"],
        "age": [20, 21, 21],
        "province": ["AB", "AB", "AB"],
        "signup_date": ["2025-01-01", "2025-01-02", "2025-01-02"],
        "income": [100, 200, 200],
    })
    res = run_all_checks(df, RULES)
    assert "duplicates" in res
    assert len(res["duplicates"]) == 2

def test_missing_required_columns_fatal():
    df = pd.DataFrame({"student_id": [1]})
    res = run_all_checks(df, RULES)
    assert res["fatal"]
