
# Business Data Cleaner

A Python utility for cleaning and normalizing customer CSV data.

## Current Features

- Loads customer data from CSV
- Normalizes customer names
- Normalizes email addresses
- Normalizes phone numbers
- Removes duplicate records
- Handles missing email values

## Tech Stack

- Python
- pandas
- openpxyl

## Setup

Create and activate a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Run:
From the project root:
```
python src/main.py
```

Project Structure:
business-data-cleaner/
- data/
- output/
- src/
	- main.py
- README.md
- requirements.txt
- .gitignore
