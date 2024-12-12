import psycopg2
from psycopg2 import sql

# Database connection parameters
db_params = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',  # or your database host
    'port': '5432'  # default PostgreSQL port
}


def delete_record(table_name, condition_column, condition_value):
    """
    Delete a record from a PostgreSQL table.

    :param table_name: Name of the table to delete from
    :param condition_column: Column to filter the rows
    :param condition_value: Value to filter the rows
    """
    try:
        # Connect to the PostgreSQL database
        with psycopg2.connect(**db_params) as conn:
            with conn.cursor() as cur:
                # Define the SQL delete query
                query = sql.SQL(
                    """
                    DELETE FROM {table}
                    WHERE {cond_col} = %s
                    """
                ).format(
                    table=sql.Identifier(table_name),
                    cond_col=sql.Identifier(condition_column)
                )

                # Execute the query
                cur.execute(query, (condition_value,))

                # Commit the transaction
                conn.commit()
                print(f"Record deleted successfully from table {table_name}.")

    except psycopg2.Error as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    delete_record(
        table_name="employees",
        condition_column="employee_id",
        condition_value=101
    )
