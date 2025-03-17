#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    datab = MySQLdb.connect(host='localhost', user=username,
                            passwd=password, db=database, port=3306)
    curso = datab.cursor()
    query = (
        "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"
        .format(state_name)
    )
    curso.execute(query)

    rows = curso.fetchall()
    for row in rows:
        print(row)
    curso.close()
    datab.close()
