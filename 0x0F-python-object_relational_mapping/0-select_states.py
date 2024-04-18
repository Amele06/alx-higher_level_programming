#!/usr/bin/python3

"""Module that lists all states from MySQL database"""
import sys
import MySQLdb


def list_states(username, password, database):
    """Lists all states from the specified MySQL database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
    """
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()

        # Execute the SQL query to fetch all states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows from the query result
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close the database connection
        if 'db' in locals() or 'db' in globals():
            db.close()


# Example usage
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
