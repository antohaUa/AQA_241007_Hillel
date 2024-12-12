# pip install psycopg2-binary

import psycopg2

from psycopg2 import sql

# Database connection parameters
DB_HOST = "192.168.150.116"
DB_PORT = "5432"
DB_NAME = "mydatabase"
DB_USER = "postgres"
DB_PASSWORD = "mysecretpassword"

# SQL query to execute
QUERY = "SELECT * FROM employees;"
#QUERY = "SELECT datname FROM pg_database WHERE datistemplate = false;"
#QUERY = "SELECT table_schema, table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE';"
# QUERY = "SELECT current_database();"
# QUERY = "SHOW search_path;"
#QUERY = "SELECT schema_name FROM information_schema.schemata;"
# QUERY = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"


def postrges_select():
    try:
        # Establish the connection
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("Connection to PostgreSQL established successfully.")

        # Create a cursor object
        cursor = connection.cursor()

        # Execute the query
        cursor.execute(QUERY)

        # Fetch the results
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        if 'connection' in locals() and connection:
            cursor.close()
            connection.close()
            print("Connection to PostgreSQL closed.")


if __name__ == "__main__":
    postrges_select()
