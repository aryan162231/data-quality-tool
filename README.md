# Data Validation & Automation Tool

A Python CLI tool that validates and cleans structured CSV/Excel datasets and generates automated issue reports and an HTML summary.

## Why this project
In real workflows, data often arrives messy (missing values, duplicates, invalid ranges). This tool automates data quality checks to improve reliability and reduce manual review.

## Features
- Accepts CSV/XLSX input
- Cleaning: trimming strings, type coercion, dropping exact duplicates
- Validation checks:
  - required columns
  - missing values
  - duplicate keys
  - allowed values (e.g., province codes)
  - numeric ranges (age, income)
  - date sanity checks (no future dates)
- Outputs:
  - cleaned CSV
  - issues CSV (rows + issue type)
  - HTML validation report

## Tech Stack
Python, pandas, openpyxl, pytest

## Setup
```bash
pip install -r requirements.txt
