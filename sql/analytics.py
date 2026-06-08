import sqlite3
import pandas as pd

conn = sqlite3.connect("data/churn.db")

query = """
SELECT Churn, COUNT(*) AS customers
FROM customers
GROUP BY Churn
"""

result = pd.read_sql(query, conn)

print(result)

conn.close()