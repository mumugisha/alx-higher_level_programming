#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    connec = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        unix_socket="/var/run/mysqld/mysqld.sock"
    )

    curs = connec.cursor()
    curs.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = curs.fetchall()
    for row in rows:
        print(row)

    curs.close()
    connec.close()
