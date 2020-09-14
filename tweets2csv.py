#  The tweets2csv.py program takes the tweets.json file created by the getTweets.py function
#   and returns a csv named tweets.csv containing the relevant information which we will
#   be processed.
#   Written by Jacob Briones

import json
import pandas as pd
import numpy as np

#  Set file path
tweets_data_path = "tweets.json"
tweets_data = []  

#  open and read in file
tweets_file = open(tweets_data_path, "r")  
for line in tweets_file:  
    # Here, the user can specify what language we want our data to have.
    try:  
        tweet = json.loads(line)
        if tweet['lang']=='en':
            tweets_data.append(tweet)  
    except:  
        continue

# Create Pandas Data Frame and specify columns.
tweets = pd.DataFrame()
tweets['Username'] = list(map(lambda tweet: tweet['user']['screen_name'], tweets_data))
tweets['Text'] = list(map(lambda tweet: tweet['text'], tweets_data))
tweets['Followers'] = list(map(lambda tweet: tweet['user']['followers_count'], tweets_data))
tweets['Friends'] = list(map(lambda tweet: tweet['user']['friends_count'], tweets_data))

# Hashtags are contained in an 'entities' object. This file may be empty,
#   so we must specify what we want to store if a tweet has no hashtags.
hashtags = []
for tweet in tweets_data:
    if len(tweet['entities']['hashtags'])>0:
        j = len(tweet['entities']['hashtags'])
        toappend = []
        
        for i in range(j):
            toappend.append(tweet['entities']['hashtags'][i]['text'])
        hashtags.append(toappend)
    else:
        hashtags.append('')

tweets['Hashtags'] = hashtags

#  If the tweet is a retweet, then the text will contain '@ RT'. 
#   This string usually does not provide any meaningful information
#   for us, so I chose to remove it. 
for i in range(len(tweets.Text)):
    if tweets.Text[i].startswith('RT @') == True:
        try:
            rtUser, retweetText = tweets.Text[i].split(':')
            tweets.Text=tweets.Text.replace(tweets.Text[i],retweetText)
        except:
            continue

# Save the pandas dataframe to a csv file.
tweets.to_csv('tweets.csv', index = False)
