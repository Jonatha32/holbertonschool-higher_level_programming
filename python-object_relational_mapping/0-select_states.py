#!/usr/bin/python3

"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    datab = MySQLdb.connect(host='localhost', user=username,
                            passwd=password, db=database)
    curs = datab.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    res = curs.fetchall()
    for row in res:
        print(row)

    curs.close()
    datab.close()
