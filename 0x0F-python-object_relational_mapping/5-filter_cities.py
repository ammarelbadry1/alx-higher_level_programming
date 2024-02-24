#!/usr/bin/python3
"""This script takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cursor = db.cursor()
    query = "SELECT c.name FROM cities AS c INNER JOIN states AS s ON \
             s.id = c.state_id WHERE s.name LIKE %s ORDER BY c.id ASC"
    params = (sys.argv[4],)
    cursor.execute(query, params)

    rows = cursor.fetchall()
    for i, row in enumerate(rows):
        if i == 0:
            print(row[0], end="")
        else:
            print(", " + row[0], end="")
    print()
    cursor.close()
    db.close()
