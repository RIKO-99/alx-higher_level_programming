#!/usr/bin/python3
""" selecting with mysqldb """
import MySQLdb
import sys


if __name__ == "__main__":
    try:
        conn = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            port=3306,
            db=sys.argv[3]
        )
    except MySQLdb.Error:
        print("error connecting")
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM states ORDER BY states.id")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
    except MySQLdb.Error:
        print("execution failed")
    cur.close()
    conn.close()
