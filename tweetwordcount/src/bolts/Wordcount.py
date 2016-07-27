from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
from time import time,ctime

from redis import StrictRedis
from psycopg2 import connect
import sys




class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.conn = connect(database="tcount", user="postgres", host="localhost", port="5432")
	self.cur = self.conn.cursor()

        self.redis = StrictRedis()


    def process(self, tup):
        word = tup.values[0]
	# Increment the local count
       	self.counts[word] += 1

	# Update if the word is already there in the table
	query = "UPDATE Tweetwordcount SET count=%s WHERE word=%s;" 
	data = (int(self.counts[word]), str(word) )
	self.cur.execute(query,data)  
	self.conn.commit()
	# Insert new value
	query = "INSERT into Tweetwordcount (word, count) SELECT %s, %s WHERE NOT EXISTS (SELECT word from Tweetwordcount Where word = %s);" 
	data = (str(word), int(self.counts[word]), str(word) )
	self.cur.execute(query,data)  
	self.conn.commit()



       	self.emit([word, self.counts[word]])
       	# Log the count - just to see the topology running
       	self.log('%s: %d' % (word, self.counts[word]))
 
