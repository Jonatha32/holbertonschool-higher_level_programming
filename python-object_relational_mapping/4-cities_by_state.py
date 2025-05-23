#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    datab = MySQLdb.connect(host='localhost', user=username,
                            passwd=password, db=database, port=3306)
    curso = datab.cursor()
    query = (
        "SELECT cities.id, cities.name, states.name FROM cities "
        "JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
    )
    curso.execute(query)
    rows = curso.fetchall()
    for row in rows:
        print(row)
    curso.close()
    datab.close()
