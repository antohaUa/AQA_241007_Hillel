import sqlite3
import csv


# Function to create tables
def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            product TEXT NOT NULL,
            quantity INTEGER,
            FOREIGN KEY (customer_id) REFERENCES Customers (customer_id)
        )
    ''')
    conn.commit()


# Function to load CSV data into the tables
def load_data(conn):
    cursor = conn.cursor()

    # Load Customers data
    with open("customers.csv", newline='') as customers_file:
        reader = csv.DictReader(customers_file)
        for row in reader:
            cursor.execute('''
                INSERT INTO Customers (customer_id, name, email)
                VALUES (?, ?, ?)
            ''', (row['customer_id'], row['name'], row['email']))

    # Load Orders data
    with open("orders.csv", newline='') as orders_file:
        reader = csv.DictReader(orders_file)
        for row in reader:
            cursor.execute('''
                INSERT INTO Orders (order_id, customer_id, product, quantity)
                VALUES (?, ?, ?, ?)
            ''', (row['order_id'], row['customer_id'], row['product'], row['quantity']))

    conn.commit()


# Function to search for orders by customer name
def search_orders_by_customer(conn, name):
    cursor = conn.cursor()
    query = '''
        SELECT Customers.name, Orders.product, Orders.quantity
        FROM Orders
        JOIN Customers ON Orders.customer_id = Customers.customer_id
        WHERE Customers.name = ?
    '''
    cursor.execute(query, (name,))
    results = cursor.fetchall()

    # Display results
    for row in results:
        print(f"Customer: {row[0]}, Product: {row[1]}, Quantity: {row[2]}")


# Main code
if __name__ == "__main__":
    # with sqlite3.connect('test.db') as connection:
    # result = connection.execute("SELECT name FROM sqlite_master;")

    # Connect to SQLite database (or create it)
    conn = sqlite3.connect("shop.db")

    # Create tables
    create_tables(conn)

    # Load data from CSV files
    load_data(conn)

    # Example search for a specific customer
    search_orders_by_customer(conn, "Alice")

    # Close connection
    conn.close()
