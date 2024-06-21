#!/usr/bin/python3
"""Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!"""

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        curs = conn.cursor()

        query = ("SELECT * FROM states WHERE BINARY name=%s "
                 "ORDER BY id ASC")
        curs.execute(query, (state_name,))

        rows = curs.fetchall()
        for row in rows:
            if row[1] == state_name:
                print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        if 'curs' in locals() and curs is not None:
            curs.close()
        if 'conn' in locals() and conn is not None:
            conn.close()
