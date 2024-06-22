#!/usr/bin/python3

import sys
import MySQLdb

def connect_to_mysql(username, password):
    try:
        return MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password
        )
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def database_exists(cursor, db_name):
    try:
        cursor.execute("SHOW DATABASES LIKE %s", (db_name,))
        return cursor.fetchone() is not None
    except MySQLdb.Error as e:
        print(f"Error checking database existence: {e}")
        return False

def fetch_cities_and_states(connection, database_name):
    try:
        cursor = connection.cursor()

        if not database_exists(cursor, database_name):
            print(f"Error: Database '{database_name}' not found. Please check if the database exists.")
            return

        connection.select_db(database_name)

        query = ("SELECT cities.id, cities.name, states.name "
                 "FROM cities "
                 "INNER JOIN states "
                 "ON cities.state_id = states.id "
                 "ORDER BY cities.id ASC;")
        cursor.execute(query)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error executing query: {e}")

    finally:
        if cursor:
            cursor.close()

def main():
    if len(sys.argv) < 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    connection = connect_to_mysql(mysql_username, mysql_password)
    if connection:
        fetch_cities_and_states(connection, database_name)
        connection.close()

if __name__ == "__main__":
    main()
