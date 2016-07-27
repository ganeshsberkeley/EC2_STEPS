#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#
import psycopg2
import sys

if ( len(sys.argv) == 3 ):
	k1 = int(sys.argv[1])
	k2 = int(sys.argv[2])
elif ( len(sys.argv) == 2 ):
	k1 = int(sys.argv[1])



try:
#	conn = psycopg2.connect(database="tcount", user="w205", password="postgres", host="54.89.138.171", port="5432")
	conn = psycopg2.connect(database="tcount", user="postgres", host="localhost", port="5432")
	print "Opened TCount Successfully"
except:
	print "I am unable to connect to the database"

cur = conn.cursor()

if ( len(sys.argv) == 3 ):
	cur.execute( "SELECT * FROM Tweetwordcount where count >= %d and count <= %d" % (k1, k2) )
	rows = cur.fetchall()
	for row in rows:
		print "Total Number of Occurances of \"%s\": %d" %(row[0], row[1])
	conn.close()
	print "Selected Range is from %d to %d" %(k1, k2)
elif ( len(sys.argv) == 2 ):
	cur.execute( "SELECT * FROM Tweetwordcount where count >= %d " % (k1) )
	rows = cur.fetchall()
	for row in rows:
		print "Total Number of Occurances of \"%s\": %d" %(row[0], row[1])
	conn.close()
	print "Starting Range is from %d " %(k1)
else:
	query = "SELECT * FROM Tweetwordcount ORDER BY word"
	cur.execute(query)
	rows = cur.fetchall()
	for row in rows:
		print "\"%s\" number of occurances: %d" %(row[0], row[1])
	conn.close()
	print "No lower and upper bound selected"
