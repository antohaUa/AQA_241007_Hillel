import sqlite3

# Connect to SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product TEXT NOT NULL,
    amount INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
''')

# Insert data
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Bob", "bob@example.com"))
cursor.execute("INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)", (1, "Laptop", 1200))
cursor.execute("INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)", (2, "Phone", 800))
cursor.execute("INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)", (1, "Tablet", 300))

# Commit changes
conn.commit()

# Select and join data
cursor.execute('''
SELECT users.name, users.email, orders.product, orders.amount
FROM users
JOIN orders ON users.id = orders.user_id
''')

# Fetch and display results
rows = cursor.fetchall()
print("Join Results:")
for row in rows:
    print(row)
#
# # Update data
# cursor.execute("UPDATE users SET email = ? WHERE name = ?", ("alice@newdomain.com", "Alice"))
# conn.commit()
#
# # Delete data
# cursor.execute("DELETE FROM orders WHERE product = ?", ("Tablet",))
# conn.commit()
#
# # Verify deletion
# cursor.execute("SELECT * FROM orders")
# print("\nOrders after deletion:")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# Close the connection
conn.close()
