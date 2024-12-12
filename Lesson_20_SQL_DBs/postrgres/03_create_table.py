import psycopg2
from psycopg2 import sql

# Database connection parameters
DB_HOST = "192.168.150.116"
DB_PORT = "5432"
DB_NAME = "mydatabase"
DB_USER = "postgres"
DB_PASSWORD = "mysecretpassword"

# SQL query to create a new table
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    department VARCHAR(50)
);
"""


def create_table():
    """Connect to the database and create the table."""
    try:
        # Establish the connection
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print(f"Connected to database: {DB_NAME}")

        # Create a cursor object
        cursor = connection.cursor()

        # Execute the CREATE TABLE query
        cursor.execute(CREATE_TABLE_QUERY)
        connection.commit()  # Commit the transaction



        print("Table 'employees' created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the cursor and connection
        if 'connection' in locals() and connection:
            cursor.close()
            connection.close()
            print(f"Connection to database {DB_NAME} closed.")


if __name__ == "__main__":
    create_table()