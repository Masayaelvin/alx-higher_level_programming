#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
	conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
	cur = conn.cursor()
	cur.execute("SELECT  * FROM states;")
	[print (state) for state in cur.fetchall()]

