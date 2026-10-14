import pandas as pd

# 1. Load the merged Excel file you just created
# Ensure the file path matches where you saved Merged_Retail_Data.xlsx
df = pd.read_excel('Merged_Retail_Data.xlsx', sheet_name='Sales_Data')

# 2. Data Cleaning & Standardization
# Convert the transaction_date column to proper datetime objects for Tableau
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# Fill any missing financial values with 0 (standard data engineering practice)
df['amount'] = df['amount'].fillna(0)

# Verify the final data structure in the terminal
print(df.info())

# 3. Export the production-ready dataset
df.to_csv('Tableau_Ready_Data.csv', index=False)
print("\nSuccess: Data cleaned and exported as Tableau_Ready_Data.csv!")