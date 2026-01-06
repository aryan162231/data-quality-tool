# Data Validation & Automation Tool

A Python CLI tool that validates and cleans structured CSV/XLSX datasets and generates an HTML report with detected issues.

## Features
- CSV / Excel input
- Data cleaning (type coercion, trimming, duplicates removal)
- Validation checks:
  - required columns
  - missing values
  - duplicate keys
  - allowed values (e.g., province codes)
  - numeric ranges (age, income)
  - date sanity checks (no future dates)
- Outputs:
  - cleaned CSV
  - issues CSV
  - HTML validation report

## Setup
```bash
pip install -r requirements.txt
