#!/usr/bin/python3
"""Lists all states with a name starting with N from hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    datab = MySQLdb.connect(host='localhost', user=username,
                            passwd=password, db=database, port=3306)
    curso = datab.cursor()
    curso.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
    rows = curso.fetchall()
    for row in rows:
        print(row)

    curso.close()
    datab.close()
