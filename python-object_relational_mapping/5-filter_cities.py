#!/usr/bin/python3
"""Lists all cities of a give state from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    datab = MySQLdb.connect(host='localhost', user=username,
                            passwd=password, db=database, port=3306)
    curs = datab.cursor()
    query = """
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    curs.execute(query, (state_name,))
    rows = curs.fetchall()
    print(", ".join([city[0] for city in rows]))
    curs.close()
    datab.close()
