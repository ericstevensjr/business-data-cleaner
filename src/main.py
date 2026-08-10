import logging
import argparse
import sys
import pandas as pd

REQUIRED_COLUMNS = {"name", "email", "phone", "amount"}

logging.basicConfig(
	level=logging.INFO,
	format="%(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)

def load_customers(filepath):
	return pd.read_csv(filepath)

def normalize_names(customers):
	customers["name"] = customers["name"].str.strip().str.title()
	return customers

def normalize_emails(customers):
	customers["email"] = (
		customers["email"]
		.fillna("missing")
		.str.strip()
		.str.lower()
	)
	return customers

def normalize_phones(customers):
	customers["phone"] = customers["phone"].str.replace(
		r"\D", "", regex=True
	)
	return customers

def normalize_amounts(customers):
	customers["amount"] = pd.to_numeric(
		customers["amount"],
		errors="coerce",
	)

	return customers

def remove_duplicates(customers):
	return customers.drop_duplicates(
		subset=["name", "email", "phone", "amount"]
	)

def export_customers(customers, filepath):
	customers.to_excel(filepath, index=False)

def generate_summary(customers):
	return {
		"total_customers": int(len(customers)),
		"total_revenue": float(customers["amount"].sum()),
		"average_revenue": float(customers["amount"].mean()),
		"missing_emails": int(
			(customers["email"] == "missing").sum()
		),
	}

def validate_columns(customers):
	missing_columns = REQUIRED_COLUMNS - set(customers.columns)
	
	if missing_columns:
		missing = ", ".join(sorted(missing_columns))
		raise ValueError(f"Missing required columns: {missing}")

def validate_amounts(customers):
	invalid_count = customers["amount"].isna().sum()
	
	if invalid_count:
		raise ValueError(
			f"Found {invalid_count} invalid amount value(s)"
		)

def parse_args():
	parser = argparse.ArgumentParser(
		description="Clean customer data and export an Excel report."
	)
	
	parser.add_argument(
		"input_file",
		help="path to the input CSV file",
	)

	parser.add_argument(
		"-o",
		"--output",
		default="output/clean_customers.xlsx",
		help="Path for the cleaned Excel output",
	)

	return parser.parse_args()

def run():
	args = parse_args()
	
	try:
		logger.info(
			"Loading customer data from %s",
			args.input_file,
		)

		customers = load_customers(args.input_file)
		validate_columns(customers)

		customers = normalize_names(customers)
		customers = normalize_emails(customers)
		customers = normalize_phones(customers)
		customers = normalize_amounts(customers)
		validate_amounts(customers)

		customers = remove_duplicates(customers)

		export_customers(customers, "output/clean_customers.xlsx")

		logger.info(
			"Exported cleaned data to %s",
			args.output,
		)

		summary = generate_summary(customers)

		print(f"Cleaned {len(customers)} customer records.")
		print(f"Total Revenue: ${summary['total_customers']:.2f}")
		print(f"Average revenue: ${summary['average_revenue']:.2f}")
		print(f"Missing emails: {summary['missing_emails']}")
		print(f"Output written to: {args.output}")
	
	except FileNotFoundError:
		print(
			f"Error: input file not found: {args.input_file}",
			file=sys.stderr,
		)
		return 1

	except pd.errors.EmptyDataError:
		print(
			"Error: input CSV is empty.",
			file=sys.stderr,
		)
		return 1
	except ValueError as exc:
		print(f"error: {exc}", file=sys.stderr)
		return 1

	except OSError as exc:
		print(f"Error writing output file: {exc}", file=sys.stderr)
		return 1

	return 0


if __name__ == "__main__":
	raise SystemExit(run())
