import json
import pandas as pd
import numpy as np
tweets_data_path = "tweets.json"
tweets_data = []  
tweets_file = open(tweets_data_path, "r")  
for line in tweets_file:  
    try:  
        tweet = json.loads(line)
        if tweet['lang']=='en':
            tweets_data.append(tweet)  
    except:  
        continue
tweets = pd.DataFrame()
tweets['Username'] = list(map(lambda tweet: tweet['user']['screen_name'], tweets_data))
tweets['Text'] = list(map(lambda tweet: tweet['text'], tweets_data))
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
tweets['Followers'] = list(map(lambda tweet: tweet['user']['followers_count'], tweets_data))
tweets['Friends'] = list(map(lambda tweet: tweet['user']['friends_count'], tweets_data))


retweetedUsers = []
for i in range(len(tweets.Text)):
    if tweets.Text[i].startswith('RT @') == True:
        try:
            rtUser, retweetText = tweets.Text[i].split(':')
            tweets.Text=tweets.Text.replace(tweets.Text[i],retweetText)
        except:
            continue
        
tweets.to_csv('twitter_trump_biden.csv', index = False)
