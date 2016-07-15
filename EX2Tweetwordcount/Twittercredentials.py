import tweepy

consumer_key = "	Xi136MPzusLFDnk4uETJnV7VD";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "e4TigozuPdDVIIJnH38pUHUmi9wJORml5jm71rkYqde274hFSi";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "754010347967614977-BVru3rQngbCMOX6yWu39lhzEFBfovaZ";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "LEp1MEp3wuR8NCF1OTd9GdJVIKU7XIemnvj2noi5eAgOB";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



