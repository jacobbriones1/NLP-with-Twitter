import numpy as np
import pandas as pd
import tweepy
import datetime
import os
import json

#  Import credentials
import credentials

from tweepy import Stream

# Set up words to track  
keywords_to_track = ['trump','biden']
#  Retrieve credentials
consumer_key = credentials.CONSUMER_KEY
consumer_secret = credentials.CONSUMER_SECRET
access_token = credentials.ACCESS_TOKEN
access_secret = credentials.ACCESS_SECRET
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


        
api = tweepy.API(auth,wait_on_rate_limit=True)
tweets = []
# file name that you want to open is the second argument
save_file = open('Oct5Tweets.json', 'a')

class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        self.save_file = tweets

    def on_data(self, tweet):
        self.save_file.append(json.loads(tweet))
        text = json.loads(tweet)
        try:
            print(str(text['text']))
        except:
            print()
        save_file.write(str(tweet))

stream = Stream(auth, CustomStreamListener(api),tweet_mode='extended')
stream.filter(track=keywords_to_track)
