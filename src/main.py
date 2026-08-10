import pandas as pd

customers = pd.read_csv("data/customers.csv")

customers["name"] = customers["name"].str.strip().str.title()
customers["email"] = customers["email"].str.strip().str.lower()

customers["phone"] = customers["phone"].str.replace(
	r"\D", "", regex=True
)

customers = customers.drop_duplicates(
	subset=["name", "email", "phone", "amount"]
)

customers["email"] = customers["email"].fillna("missing")

print(customers)
