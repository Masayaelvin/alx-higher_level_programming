#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
	db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
	cur = db.cursor()
	query = ("SELECT name FROM cities\
			WHERE state_id = (\
			SELECT id FROM states\
			WHERE name = %s )")
	name = sys.argv[4]
	cur.execute(query, (name,))
	results = cur.fetchall()
	
	[print(city, end="") for city in results]

