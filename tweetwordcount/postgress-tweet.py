#!/usr/bin/python
import psycopg2

conn = psycopg2.connect(database="Tcount", user="root", password="pass", host="54.198.167.194", port="8080")
print "Opened TCount Successfully"
