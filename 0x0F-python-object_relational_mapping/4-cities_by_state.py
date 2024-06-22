#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb


def connect_to_mysql(username, password, database):
    try:
        return MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def fetch_cities_and_states(connection):
    try:
        cursor = connection.cursor()

        query = (
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "INNER JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC;"
        )
        cursor.execute(query)

        rows = cursor.fetchall()
        for row in rows:
            print(f"{row[0]}: {row[1]}, {row[2]}")

    except MySQLdb.Error as e:
        print(f"Error executing query: {e}")

    finally:
        if cursor:
            cursor.close()


def main():
    if len(sys.argv) != 4:
        print(
            "Usage: python 4-cities_by_state.py <mysql_username> "
            "<mysql_password> <database_name>"
        )
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    connection = connect_to_mysql(
        mysql_username,
        mysql_password,
        database_name
    )

    if connection:
        try:
            fetch_cities_and_states(connection)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            connection.close()


if __name__ == "__main__":
    main()
