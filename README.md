
# Business Data Cleaner

A Python command-line tool for cleaning messy customer CSV data and exporting a standardized Excel file with summary metrics.

## Current Features

- Normalizes customer names
- Normalizes email addresses
- Standardizes phone numbers
- Removes duplicate records
- Detects missing required columns
- Validates numeric transaction amounts
- Handles common file errors
- Generates custoemr/revenue summary metrics
- Exports cleaned data to Excel
- Includes automated pytest coverage

## Example

Input:
|   name   |       email      |      phone     | amount |
| -------- | ---------------- | -------------- | ------ |
|john smith| JOHN@example.com | (904) 555-1234 | 125.50 |

Output:
|   name   |       email      |   phone    | amount |
| -------- | ---------------- | ---------- | ------ |
|John Smith| john@example.com | 9045551234 | 125.50 |

## Installation
```
git clone https://github.com/ericstevensjr/business-data-cleaner
cd business-data-cleaner
python 3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Usage
python src/main.py data/customers.csv

## Custom output path:
python src/main.py data/customers.csv --ouput output/clean_customers.xlsx

## Testing
python -m pytest
```

## Tech Stack
- Python
- pandas
- opnepyxl
- pytest
- Git/Github

