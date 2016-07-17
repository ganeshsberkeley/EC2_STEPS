import tweepy

consumer_key = "Xi136MPzusLFDnk4uETJnV7VD";


consumer_secret = "e4TigozuPdDVIIJnH38pUHUmi9wJORml5jm71rkYqde274hFSi";

access_token = "754010347967614977-BVru3rQngbCMOX6yWu39lhzEFBfovaZ";

access_token_secret = "LEp1MEp3wuR8NCF1OTd9GdJVIKU7XIemnvj2noi5eAgOB";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



