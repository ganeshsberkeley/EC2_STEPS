#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#
import psycopg2
import sys

if ( len(sys.argv) == 2 ):
	input = str(sys.argv[1])


try:
#	conn = psycopg2.connect(database="tcount", user="w205", password="postgres", host="54.89.138.171", port="5432")
	conn = psycopg2.connect(database="tcount", user="postgres", host="localhost", port="5432")
	print "Opened TCount Successfully"
except:
	print "I am unable to connect to the database"

cur = conn.cursor()
#cur.execute("DROP TABLE IF EXISTS Tweetwordcount")
#cur.execute("CREATE TABLE Tweetwordcount (word TEXT PRIMARY KEY     NOT NULL, count INT     NOT NULL)")

if ( len(sys.argv) == 2 ):
	query = "SELECT * FROM Tweetwordcount where word = %s"
	cur.execute( "SELECT * FROM Tweetwordcount where word = '%s'" % (input) )
	rows = cur.fetchall()
	for row in rows:
		print "Total Number of Occurances of \"%s\": %d" %(row[0], row[1])
	conn.close()
else:
	query = "SELECT * FROM Tweetwordcount ORDER BY word"
	cur.execute(query)
	rows = cur.fetchall()
	for row in rows:
		print "\"%s\" number of occurances: %d" %(row[0], row[1])
	conn.close()

