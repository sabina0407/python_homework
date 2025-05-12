import pandas as pd
import sqlite3

# Connect to the lesson.db database
with sqlite3.connect("../db/lesson.db") as conn:
    # SQL Query
    sql_statement = """
    SELECT 
        line_items.line_item_id,
        line_items.quantity,
        products.product_id,
        products.product_name,
        products.price
    FROM 
        line_items
    JOIN 
        products
    ON 
        line_items.product_id = products.product_id
    """

    # Load SQL results into a DataFrame
    df = pd.read_sql_query(sql_statement, conn)

# Print the first 5 lines of the DataFrame
print("\nInitial DataFrame:")
print(df.head())

# Add a 'total' column
df['total'] = df['quantity'] * df['price']

# Print the first 5 lines of the DataFrame
print("\nDataFrame with 'total' column:")
print(df.head())

# Group by the product_id
summary = df.groupby('product_id').agg({'line_item_id': 'count', 'total': 'sum', 'product_name': 'first'}).reset_index()

# Sort by product_name
summary = summary.sort_values(by='product_name')

# Print grouped DataFrame
print("\nGrouped and Sorted Summary:")
print(summary.head())

# Write to CSV
summary.to_csv("order_summary.csv", index=False)
print("\nSummary saved to 'order_summary.csv'.")
