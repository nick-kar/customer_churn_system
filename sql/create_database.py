import pandas as pd
import sqlite3

# Load CSV
df = pd.read_csv(
    "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

# Create database
conn = sqlite3.connect("data/churn.db")

# Save table
df.to_sql(
    "customers",
    conn,
    if_exists="replace",
    index=False
)

# Verify
cursor = conn.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM customers"
)

print("Rows in database:", cursor.fetchone()[0])

conn.close()

print("Database created successfully.")