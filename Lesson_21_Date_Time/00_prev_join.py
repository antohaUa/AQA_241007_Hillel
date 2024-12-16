import sqlite3

# Connect to SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect("join.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS A (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS B (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    score INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS TableC (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    salary INTEGER NOT NULL
)
''')

# Insert data
cursor.execute("INSERT INTO A (name) VALUES (?)", ("David",))
cursor.execute("INSERT INTO A (name) VALUES (?)", ("Anna",))
cursor.execute("INSERT INTO A (name) VALUES (?)", ("George",))
cursor.execute("INSERT INTO B (score) VALUES (?)", (80,))
cursor.execute("INSERT INTO B (score) VALUES (?)", (90,))
cursor.execute("INSERT INTO B (score) VALUES (?)", (100,))
cursor.execute("INSERT INTO TableC (salary) VALUES (?)", (2000,))
cursor.execute("INSERT INTO TableC (salary) VALUES (?)", (3000,))

# Commit changes
conn.commit()

# # Select and join data
# cursor.execute('''
# SELECT A.id, A.name, B.score
# FROM A
# LEFT JOIN B
# ON A.id = B.id;
# ''')
#
# # Fetch and display results
# rows = cursor.fetchall()
# print("Left Join Results #1:")
# for row in rows:
#     print(row)
#
# cursor.execute('''
# SELECT A.id, A.name, B.score
# FROM A
# JOIN B
# ON A.id = B.id;
# ''')
#
# # Fetch and display results
# rows = cursor.fetchall()
# print("Inner Join Results #1:")
# for row in rows:
#     print(row)
# print('=' * 50)

# Select and join data
cursor.execute('''
SELECT A.id, A.name, TableC.salary
FROM A
LEFT JOIN TableC
ON A.id = TableC.id;
''')

# Fetch and display results
rows = cursor.fetchall()
print("Left Join Results #2:")
for row in rows:
    print(row)

cursor.execute('''
SELECT A.id, A.name, TableC.salary
FROM A
JOIN TableC
ON A.id = TableC.id;
''')

# Fetch and display results
rows = cursor.fetchall()
print("Inner Join Results #2:")
for row in rows:
    print(row)

# Close the connection
conn.close()
