(ns tweetwordcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn tweetwordcount [options]
[
	;; spout configuration (3 spouts)
    	{"tweet-spout1" (python-spout-spec
          	options
          	"spouts.tweets.Tweets"
          	["tweet"]
          	:p 3
        	)
    	"tweet-spout2" (python-spout-spec
          	options
          	"spouts.tweets.Tweets"
          	["tweet"]
          	:p 3
        	)
    	"tweet-spout3" (python-spout-spec
        	options
          	"spouts.tweets.Tweets"
          	["tweet"]
          	:p 3
          	)
    	}
    	;; bolt configuration
    	;; 3 Parse bolts
    	{"parse-tweet-bolt1" (python-bolt-spec
          	options
          	{"tweet-spout1" :shuffle}
          	"bolts.parse.ParseTweet"
          	["word"]
          	:p 3
          	)
    	"parse-tweet-bolt2" (python-bolt-spec
          	options
          	{"tweet-spout2" :shuffle}
          	"bolts.parse.ParseTweet"
          	["word"]
          	:p 3
          	)
    	"parse-tweet-bolt3" (python-bolt-spec
          	options
          	{"tweet-spout3" :shuffle}
          	"bolts.parse.ParseTweet"
          	["word"]
          	:p 3
          	)
     	"count-bolt1" (python-bolt-spec
          	options
          	{"parse-tweet-bolt1" ["word"]
          	"parse-tweet-bolt2" ["word"]}
          	"bolts.Wordcount.WordCounter"
          	["word" "count"]
          	:p 3
          	)
     	"count-bolt2" (python-bolt-spec
          	options
          	{"parse-tweet-bolt3" ["word"]}
          	"bolts.Wordcount.WordCounter"
          	["word" "count"]
          	:p 3
          	)
	}
]
)
