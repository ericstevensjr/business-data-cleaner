import pandas as pd

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

def main():
	customers = load_customers("data/customers.csv")
	customers = normalize_names(customers)
	customers = normalize_emails(customers)
	customers = normalize_phones(customers)
	customers = remove_duplicates(customers)

	export_customers(customers, "output/clean_customers.xlsx")

	summary = generate_summary(customers)

	print(f"Cleaned {len(customers)} customer records.")
	print(f"Total Revenue: ${summary['total_customers']:.2f}")
	print(f"Average revenue: ${summary['average_revenue']:.2f}")
	print(f"Missing emails: {summary['missing_emails']}")

if __name__ == "__main__":
	main()
