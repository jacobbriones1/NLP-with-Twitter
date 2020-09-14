import numpy as np
import pandas as pd
import tweepy
import datetime
import os
import json
#  For authenticating Twitter API
import credentials
# For streaming live tweets
from tweepy import Stream

# keywords_to_track: list of strings to watch for.
def getTweets(ketwords_to_track):
        #  Retrieve credentials
        consumer_key = credentials.CONSUMER_KEY
        consumer_secret = credentials.CONSUMER_SECRET
        access_token = credentials.ACCESS_TOKEN
        access_secret = credentials.ACCESS_SECRET
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        
        #  Authorization 
        auth.set_access_token(access_token, access_secret)
        
        # Instantiate Twitter API.
        # NOTE:Twitter limits the amount of data that a user may stream.
        #   if a user revcieves a rate_limit warning, then the user must 
        #   wait one hour before accessing data. The wait_on_rate_limit
        #   parameter ensures that our program will not terminate if this
        #   error occurs.
        api = tweepy.API(auth, wait_on_rate_limit=True,)
        tweets = []
        # file name that you want to open is the second argument
        save_file = open('tweets.json', 'a')

        class CustomStreamListener(tweepy.StreamListener):
            def __init__(self, api):
                self.api = api
                super(tweepy.StreamListener, self).__init__()
                self.save_file = tweets

            def on_data(self, tweet):
                self.save_file.append(json.loads(tweet))
                print(tweet)
                save_file.write(str(tweet))

        stream = Stream(auth, CustomStreamListener(api))
        stream.filter(track=keywords_to_track)







 
