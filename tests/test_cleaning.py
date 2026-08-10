import pandas as pd
import pytest

from src.main import (
	normalize_names,
	normalize_emails,
	normalize_phones,
	remove_duplicates,
)

def test_normalize_names():
	df = pd.DataFrame({"name": [" john smith ", "JANE DOE"]})

	result = normalize_names(df)

	assert result["name"].tolist() == ["John Smith", "Jane Doe"]

def test_normalize_emails():
	df = pd.DataFrame(
		{"email": [" JOHN@EXAMPLE.COM ", None]}
	)

	result = normalize_emails(df)

	assert result["email"].tolist() == [
		"john@example.com",
		"missing",
	]

def test_normalize_phones():
	df = pd.DataFrame(
		{"phone": ["(904) 555-1234", "904-555-9876"]}
	)

	result = normalize_phones(df)

	assert result["phone"].tolist() == [
		"9045551234",
		"9045559876",
	]

def test_remove_duplicates():
	df = pd.DataFrame(
		{
			"name": ["John Smith", "John Smith"],
			"email": ["john@example.com", "john@example.com"],
			"phone": ["9045551234", "9045551234"],
			"amount": [125.50, 125.50],
		}
	)

	result = remove_duplicates(df)

	assert len(result) == 1

def test_export_customers(tmp_path):
	df = pd.DataFrame(
		{
			"name": ["John Smith"],
			"email": ["john@example.com"],
			"phone": ["9045551234"],
			"amount": [125.50],
		}
	)
	
	output_file = tmp_path / "customers.xlsx"
	
	from src.main import export_customers

	export_customers(df, output_file)

	assert output_file.exists()

def test_generate_summary():
	df = pd.DataFrame(
		{
			"name": ["John Smith", "Jane Doe"],
			"email": ["john@example.com", "missing"],
			"phone": ["9045551234", "9055557876"],
			"amount": [100.0, 200.0],
		}

	)
	
	from src.main import generate_summary

	result = generate_summary(df)

	assert result["total_customers"] == 2
	assert result["total_revenue"] == 300.0
	assert result["average_revenue"] == 150.0
	assert result["missing_emails"] == 1

def test_validate_columns_raises_for_missing_column():
	df = pd.DataFrame(
		{
			"name": ["John Smith"],
			"email": ["john@example.com"],
			"amount": [100.0],
		}
	)

	from src.main import validate_columns

	with pytest.raises(ValueError, match="phone"):
		validate_columns(df)
