import tweepy
import datetime
import os
import json
import sys
from tweepy import Stream


def get_credentials(file_path=None):
    """Retrieve credentials from credentials.py file in dir
        specified by filepath"""
    if file_path:
        sys.path.insert(1, file_path)
    import credentials
    
    consumer_key = credentials.CONSUMER_KEY
    consumer_secret = credentials.CONSUMER_SECRET
    access_token = credentials.ACCESS_TOKEN
    access_secret = credentials.ACCESS_SECRET
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

class CustomStreamListener(tweepy.StreamListener):
    """Class for downloading tweets in real time using the Twitter API."""
    
    def __init__(self, api=None, file_path=None):
        """Initialize a custom stream listener. The default file_path is set to the current directory.
            If an api is not specified upon initialization, then the file_path directory must contain a 
            credentials.py file which define CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, and ACCESS_SECRET"""
        
        self.auth = get_credentials(file_path)
        
        if not api:
            self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
            
        else:
            self.api = api
            
        super(tweepy.StreamListener, self).__init__()
        self.save_file = []

        self.file_name = datetime.datetime.today().strftime('%Y-%m-%d')+'-tweets.json'

    
    def on_data(self, tweet):
        """The on_data method of a stream listener receives all
            messages and calls functions according to the message type"""
        save_file = open(self.file_name, 'a')

        self.save_file.append(json.loads(tweet))
        text = json.loads(tweet)
        
        try:
            print(str(text['text']))
        except:
            print()
        save_file.write(str(tweet))

    def collect(self, keywords:list):
        """Collect tweets containing keywords"""
        stream = Stream(self.auth,
                        CustomStreamListener(self.api),
                        tweet_mode = 'extended')
        stream.filter(track=keywords)
