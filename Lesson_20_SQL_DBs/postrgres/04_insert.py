import psycopg2

# Database connection parameters
DB_HOST = "192.168.150.116"
DB_PORT = "5432"
DB_NAME = "mydatabase"
DB_USER = "postgres"
DB_PASSWORD = "mysecretpassword"

# SQL query to insert data into the employees table
INSERT_QUERY = """
INSERT INTO employees (name, age, department)
VALUES (%s, %s, %s);
"""


def insert_employee(name, age, department):
    """Insert a new employee record into the employees table."""
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

        # Data to insert
        employee_data = (name, age, department)

        # Execute the INSERT query with the provided data
        cursor.execute(INSERT_QUERY, employee_data)
        connection.commit()  # Commit the transaction

        print(f"Employee {name} inserted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the cursor and connection
        if 'connection' in locals() and connection:
            cursor.close()
            connection.close()
            print(f"Connection to database {DB_NAME} closed.")


if __name__ == "__main__":
    # Example: Insert a new employee
    insert_employee('John Doe', 30, 'Marketing')
    insert_employee('Dana Li', 28, 'Marketing')