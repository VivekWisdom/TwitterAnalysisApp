# this will store user timeline tweet data in json format.

##############################################
#####      2.3 Storing Data         #########
#############################################

from api_access import api;
import tweepy;
import json;

def process_or_store(tweet):
	with open('data/my_tweets.json','a') as mt:
		mt.write(json.dumps(tweet)+'\n')

for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)
    #we can print tweets to console too.
    #print(tweet);
