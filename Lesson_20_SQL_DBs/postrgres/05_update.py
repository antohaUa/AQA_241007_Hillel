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


def update_record(table_name, set_column, set_value, condition_column, condition_value):
    """
    Update a record in a PostgreSQL table.

    :param table_name: Name of the table to update
    :param set_column: Column to set a new value
    :param set_value: New value to set
    :param condition_column: Column to filter the rows
    :param condition_value: Value to filter the rows
    """
    try:
        # Connect to the PostgreSQL database
        with psycopg2.connect(**db_params) as conn:
            with conn.cursor() as cur:
                # Define the SQL update query
                query = sql.SQL(
                    """
                    UPDATE {table}
                    SET {set_col} = %s
                    WHERE {cond_col} = %s
                    """
                ).format(
                    table=sql.Identifier(table_name),
                    set_col=sql.Identifier(set_column),
                    cond_col=sql.Identifier(condition_column)
                )

                # Execute the query
                cur.execute(query, (set_value, condition_value))

                # Commit the transaction
                conn.commit()
                print(f"Record updated successfully in table {table_name}.")

    except psycopg2.Error as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    update_record(
        table_name="employees",
        set_column="salary",
        set_value=70000,
        condition_column="employee_id",
        condition_value=101
    )
