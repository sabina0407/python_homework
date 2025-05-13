# Task 1: Complex JOINs with Aggregation

import sqlite3

try:
    # Connect to the database
    with sqlite3.connect('../db/lesson.db') as conn:
        cursor = conn.cursor()

        # Get total price
        query = """
        SELECT o.order_id, SUM(l.quantity * p.price) AS total_price
        FROM orders o
        JOIN line_items l ON o.order_id = l.order_id
        JOIN products p ON l.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id
        LIMIT 5;
        """
        
        cursor.execute(query)
        results = cursor.fetchall()

        # Print the results
        print("Total price for each order:")
        for order_id, total_price in results:
            print(f"Order ID: {order_id}, Total Price: {total_price:.2f}")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")


# Task 2: Understanding Subqueries

try:
    with sqlite3.connect('../db/lesson.db') as conn:
        cursor = conn.cursor()

        query = """
        SELECT c.customer_name, AVG(order_totals.total_price) AS average_total_price
        FROM customers c
        LEFT JOIN (
            SELECT o.customer_id AS customer_id_b, SUM(l.quantity * p.price) AS total_price
            FROM orders o
            JOIN line_items l ON o.order_id = l.order_id
            JOIN products p ON l.product_id = p.product_id
            GROUP BY o.order_id
        ) AS order_totals ON c.customer_id = order_totals.customer_id_b
        GROUP BY c.customer_id
        """

        cursor.execute(query)
        results = cursor.fetchall()

        # Print the results
        print("\nAverage total price for each customer:")
        for customer_name, avg_total in results:
            # print(f"{customer_name}: {avg_total:.2f}")
            print(f"{customer_name}: {avg_total}")


except sqlite3.Error as e:
    print(f"An error occurred: {e}")


# Task 3: An Insert Transaction Based on Data

try:
    with sqlite3.connect('../db/lesson.db') as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        # Look up customer_id & employee_id
        cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
        customer_id = cursor.fetchone()[0]

        cursor.execute("""
            SELECT employee_id FROM employees
            WHERE first_name = 'Miranda' AND last_name = 'Harris'
        """)
        employee_id = cursor.fetchone()[0]

        # Get 5 least expensive products
        cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
        product_ids = [row[0] for row in cursor.fetchall()]

        # Insert a new order
        cursor.execute("""
            INSERT INTO orders (customer_id, employee_id, date)
            Values (?, ?, DATE('now'))
            RETURNING order_id
        """, (customer_id, employee_id))
        order_id = cursor.fetchone()[0]

        # Insert line items for the new order
        
        for product_id in product_ids:
            cursor.execute("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, ?)
            """, (order_id, product_id, 10))

        conn.commit()

        # Select the new order
        cursor.execute("""
            SELECT l.line_item_id, l.quantity, p.product_name
            FROM line_items l
            JOIN products p ON l.product_id = p.product_id
            WHERE l.order_id = ?
        """, (order_id,))
        results = cursor.fetchall()

        # Print the results
        print(f"\nLine items for the new order (Order ID: {order_id}):")
        for line_item_id, quantity, product_name in results:
            print(f"Line Item ID: {line_item_id}, Quantity: {quantity}, Product Name: {product_name}")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

# Task 4: Aggregation with HAVING

try:
    with sqlite3.connect('../db/lesson.db') as conn:
        cursor = conn.cursor()

        query = """
        SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(o.order_id) > 5
        """

        cursor.execute(query)
        results = cursor.fetchall()

        # Print the results
        print("\nEmployees with more than 5 orders:")
        for employee_id, first_name, last_name, order_count in results:
            print(f"Employee ID: {employee_id}, Name: {first_name} {last_name}, Order Count: {order_count}")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")