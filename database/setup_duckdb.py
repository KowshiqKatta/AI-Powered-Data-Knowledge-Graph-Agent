import duckdb
import pandas as pd
import os

# Get the path relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "..", "data")

conn = duckdb.connect("analytics.db")

customers = pd.read_csv(os.path.join(data_dir, "customers.csv"))
orders = pd.read_csv(os.path.join(data_dir, "orders.csv"))
products = pd.read_csv(os.path.join(data_dir, "products.csv"))

conn.execute("CREATE TABLE customers AS SELECT * FROM customers")
conn.execute("CREATE TABLE orders AS SELECT * FROM orders")
conn.execute("CREATE TABLE products AS SELECT * FROM products")

print("Database setup complete.")
