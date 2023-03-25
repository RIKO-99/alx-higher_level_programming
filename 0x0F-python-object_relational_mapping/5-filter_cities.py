#!/usr/bin/python3

""" This module takes in the name of a state as an argument
and lists all cities of that state in the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost',
                         port=3306, user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.name\
                FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id", (sys.argv[4], ))

    rows = cur.fetchall()

    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()
