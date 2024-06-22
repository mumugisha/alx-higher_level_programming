#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa.
"""

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
        query = (
            "SELECT cities.name "
            "FROM cities "
            "INNER JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id ASC;"
        )
        curs.execute(query, (state_name,))

        rows = curs.fetchall()
        rows = [row[0] for row in rows]
        print(", ".join(rows))
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if 'curs' in locals():
            curs.close()
        if 'connec' in locals():
            connec.close()
