#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        connec = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )
        curs = connec.cursor()
        query = (
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "INNER JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC;"
        )

        curs.execute(query)
        rows = curs.fetchall()
        for row in rows:
            print(row)

        curs.close()
        connec.close()
    except MySQLdb.Error as e:
        print(f"Error {e}")
    except IndexError:
        print("Usage: ./script.py <mysql_username> <mysql_password> <database_name>")
