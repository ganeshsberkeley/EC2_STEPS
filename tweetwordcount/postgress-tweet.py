#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#
import psycopg2

#try:
conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="54.89.138.171", port="5432")
print "Opened TCount Successfully"
#except:
#    print "I am unable to connect to the database"
