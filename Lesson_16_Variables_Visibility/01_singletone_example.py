import sqlite3


class DatabaseConnection(object):
    _instance = None

    def __del__(self):
        print('Finish')

    def __new__(cls, db_file):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self._cursor = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_file)
            print("Connected to database.")
            self._cursor = self.connection.cursor()
        else:
            print("Already connected to database.")

    def create_table(self):
        res = self._cursor.execute('''CREATE TABLE IF NOT EXISTS users
                                      (id INTEGER PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT)''')
        print('Table created')
        return res

    def insert(self, users):
        res = self._cursor.executemany('INSERT INTO users (firstname, lastname) VALUES (?, ?)', users)
        print('Users were inserted')
        self.connection.commit()
        print('Db updated')
        return res

    def read(self):
        # Read the data from the table
        self._cursor.execute('SELECT * FROM users')
        res = self._cursor.fetchall()
        return res

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
            print("Disconnected from database.")
        else:
            print("No connection to close.")


# Usage example
db_file_name = "example.db"
db_users = [('John', 'Doe'),
            ('Jane', 'Smith'),
            ('Tom', 'Hanks')]

# Create a new instance of DatabaseConnection
db1 = DatabaseConnection(db_file_name)
# db1.connect()
# db1.create_table()
# db1.insert(db_users)
# result = db1.read()
# print(result)
print(id(db1))
# db1.disconnect()

# Try creating another instance of DatabaseConnection
# It will return the same instance as before
db2 = DatabaseConnection(db_file_name)
# db2.connect()
# result = db1.read()
# print(result)
print(id(db2))
#
# # Disconnect from the database


db3 = DatabaseConnection(db_file_name)
# db2.connect()
# result = db1.read()
# print(result)
print(id(db3))

db1.disconnect()
db2.disconnect()
db3.disconnect()

