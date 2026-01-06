# src/rules.py

RULES = {
    "required_columns": ["student_id", "name", "email", "age", "province", "signup_date", "income"],
    "unique_columns": ["student_id"],
    "allowed_values": {
        "province": ["AB", "BC", "SK", "MB", "ON", "QC", "NS", "NB", "NL", "PE", "NT", "NU", "YT"]
    },
    "ranges": {
        "age": {"min": 16, "max": 100},
        "income": {"min": 0, "max": 500000}
    }
}
