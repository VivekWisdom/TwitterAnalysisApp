#This program fetches all the tweets from my profile.
# TO use Tweepy you have to install it by command "pip install tweepy"

##############################################
#####      2.2 Accessing Data       #########
#############################################
import tweepy
from tweepy import OAuthHandler
import config
import json

auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
api = tweepy.API(auth)
