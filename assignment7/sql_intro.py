import sqlite3

# Functions to add data to the database
def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")

def add_magazine(cursor, name, publisher_name):
    try:
        # Find publisher_id 
        cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
        result = cursor.fetchone()
        if result:
            publisher_id = result[0]
            cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        else:
            print(f"Publisher '{publisher_name}' not found.")
    except sqlite3.IntegrityError:
        print(f"Magazine '{name}' already exists.")

def add_subscriber(cursor, name, address):
    try:
        # Check for duplicates
        cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
        result = cursor.fetchone()
        if result:
            print(f"Subscriber '{name}' at '{address}' already exists.")
        else:
            cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
    except sqlite3.IntegrityError:
        print(f"Error inserting subscriber '{name}'.")

def add_subscription(cursor, subscriber_name, subscriber_address, magazine_name, expiration_date):
    try:
        # Find subscriber_id
        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?", (subscriber_name, subscriber_address))
        sub_result = cursor.fetchone()
        if not sub_result:
            print(f"Subscriber '{subscriber_name}' at '{subscriber_address}' not found.")
            return
        subscriber_id = sub_result[0]

        # Find magazine_id
        cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
        mag_result = cursor.fetchone()
        if not mag_result:
            print(f"Magazine '{magazine_name}' not found.")
            return
        magazine_id = mag_result[0]

        # Check for existing subscription
        cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
        sub_exist = cursor.fetchone()
        if sub_exist:
            print(f"Subscription already exists for '{subscriber_name}' to '{magazine_name}'.")
        else:
            cursor.execute(
                "INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
                (subscriber_id, magazine_id, expiration_date)
            )
    except sqlite3.IntegrityError as e:
        print(f"Error inserting subscription: {e}")

try:
    # Connect to the database
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        # Create tables 
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
        )
        """)

        print("Tables created successfully.")

        # Populate tables:

        add_publisher(cursor, "Penguin Random House")
        add_publisher(cursor, "HarperCollins")
        add_publisher(cursor, "Macmillan")

        add_magazine(cursor, "Costco Connection", "Penguin Random House")
        add_magazine(cursor, "US Weekly", "HarperCollins")
        add_magazine(cursor, "National Geographic", "Macmillan")

        add_subscriber(cursor, "Anna Swan", "657 Austin Street")
        add_subscriber(cursor, "Steve Johnson", "396 Burns Street")
        add_subscriber(cursor, "Mira Turner", "53 Woodland Avenue")

        add_subscription(cursor, "Anna Swan", "657 Austin Street", "Costco Connection", "2025-12-31")
        add_subscription(cursor, "Steve Johnson", "396 Burns Street", "US Weekly", "2025-06-30")
        add_subscription(cursor, "Mira Turner", "53 Woodland Avenue", "National Geographic", "2026-01-15")

        # commit!
        conn.commit()
        print("Sample data inserted successfully.")

    
        # Querying the database

        print("\nAll Subscribers:")
        cursor.execute("SELECT * FROM subscribers")
        subscribers = cursor.fetchall()
        for subscriber in subscribers:
            print(subscriber)

        print("\nAll Magazines:")
        cursor.execute("SELECT * FROM magazines ORDER BY name ASC")
        magazines = cursor.fetchall()
        for magazine in magazines:
            print(magazine)

        print("\nMagazines published by 'Penguin Random House':")
        cursor.execute("""
        SELECT magazines.magazine_id, magazines.name FROM magazines 
        JOIN publishers ON magazines.publisher_id = publishers.publisher_id
        WHERE publishers.name = ?
        """, ("Penguin Random House",))
        publisher_magazines = cursor.fetchall()
        for mag in publisher_magazines:
            print(mag)


except sqlite3.Error as e:
    print(f"An error occurred: {e}")
