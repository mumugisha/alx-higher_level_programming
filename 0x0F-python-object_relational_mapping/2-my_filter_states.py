#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument."""

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        connec = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )
        curs = connec.cursor()
        query = ("SELECT * FROM states WHERE name=%s ORDER BY states.id ASC")
        curs.execute(query, (state_name,))
        rows = curs.fetchall()
        for row in rows:
            if row[1] == state_name:
                print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if 'curs' in locals():
            curs.close()
        if 'connec' in locals():
            connec.close()
