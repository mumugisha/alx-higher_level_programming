#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb


def main():
    if len(sys.argv) != 4:
        print("Usage: python 4-cities_by_state.py <mysql_username> "
              "<mysql_password> <database_name>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()
        cursor.execute(
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "INNER JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC;"
        )

        for row in cursor.fetchall():
            print(f"{row[0]}: {row[1]}, {row[2]}")

        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
