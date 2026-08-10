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

def main():
	customers = load_customers("data/customers.csv")
	customers = normalize_names(customers)
	customers = normalize_emails(customers)
	customers = normalize_phones(customers)
	customers = remove_duplicates(customers)

	print(customers)
	print(customers.shape)

if __name__ == "__main__":
	main()
