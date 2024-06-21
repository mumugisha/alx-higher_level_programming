#!/usr/bin/python3
"""Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa."""

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        connec = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        curs = connec.cursor()
        query = ("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                 "ORDER BY states.id ASC")
        curs.execute(query)

        rows = curs.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if 'curs' in locals():
            curs.close()
        if 'connec' in locals():
            connec.close()
