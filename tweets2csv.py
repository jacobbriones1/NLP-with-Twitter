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
    try:  
        tweet = json.loads(line)
        if tweet['lang']=='en':
            tweets_data.append(tweet)  
    except:  
        continue

tweets = pd.DataFrame()
tweets['Username'] = list(map(lambda tweet: str(tweet['user']['screen_name']), tweets_data))
text = []
for tweet in tweets_data:
    if tweet['is_quote_status']==True and not 'retweeted_status' in tweet:
            # check if quoted tweet's text has been truncated before recording
        try:
            extended=tweet['quoted_status']['extended_tweet']
            full = extended['full_text']
            
        except:
            if 'extended_tweet' in tweet:
                full = tweet['extended_tweet']['full_text']
            else:
                full = tweet['text']
            
        text.append(full)
            
    elif 'retweeted_status' in tweet and tweet['is_quote_status']==False:
        try:
            extended=tweet['retweeted_status']['extended_tweet']
            full = extended['full_text']

        except:
            if 'extended_tweet' in tweet:
                full = tweet['extended_tweet']['full_text']
            else:
                full = tweet['text']
            
        text.append(full)

    elif 'retweeted_staus' in tweet and tweet['is_quote_status']==True:
        try:
            extended=tweet['retweeted_status']['extended_tweet']
            full = extended['full_text']
        except:
            try:
                extended=tweet['quoted_status']['extended_tweet']
                full = extended['full_text']
            except:  
                full = tweet['retweeted_status']['text']
            
        text.append(full)
                
    elif tweet['truncated'] ==True and tweet['is_quote_status']==False and not 'retweeted_status' in tweet:
        text.append(tweet['extended_tweet']['full_text'])
    else:
        text.append(tweet['text'])
                    
tweets['Text'] = text

#  Get Hashtags
hashtags = []
for tweet in tweets_data:
    if len(tweet['entities']['hashtags'])>0:
        j = len(tweet['entities']['hashtags'])
        toappend = []
        for i in range(j):
            toappend.append(str(tweet['entities']['hashtags'][i]['text']))
        hashtags.append(toappend)
    else:
        hashtags.append('')
tweets['Hashtags'] = hashtags

#  Get user location
location = []
for tweet in tweets_data:
    if tweet['user']['location']!=None:
        loc = str(tweet['user']['location'])
        location.append(loc.lower())
    else:
        location.append('')
        
tweets['Location']=location

quoted =[]
retweeted = []
times_quoted = []
times_retweeted = []
quoted_users = []
retweeted_users = []
for tweet in tweets_data:
    if tweet['is_quote_status']==True:
        quoted.append('True')
        try:
            quoted_tweet= tweet['quoted_status']
            quoted_user = str(quoted_tweet['user']['screen_name'])
            times_quoted.append(int(quoted_tweet['quote_count']))
            quoted_users.append(quoted_user)
        except:
            if tweet['quote_count']>0:
                times_quoted.append(int(tweet['quote_count']))
            else:
                times_quoted.append(int(0))
            quoted_users.append('')
            
        
    elif tweet['is_quote_status']==False and tweet['quote_count']>0:
        quoted.append('False')
        times_quoted.append(int(tweet['quote_count']))
        quoted_users.append('')
    else:
        quoted.append('False')
        times_quoted.append(0)
        quoted_users.append('')
    try:
        if tweet['retweeted_status']!= None:
            Retweet = tweet['retweeted_status']
    except:
        Retweet = None
        
    if Retweet != None: 
        retweeted.append('True')
        times_retweeted.append(int(Retweet['retweet_count']))
        retweeted_users.append(str(Retweet['user']['screen_name']))
        
    else:
        retweeted.append('False')
        
        times_retweeted.append(int(0))
        retweeted_users.append('')
tweets['Quoted'] = quoted
tweets['Retweeted'] = retweeted
tweets['Quote Count'] = times_quoted
tweets['Quoted User'] = quoted_users
tweets['Retweet Count'] = times_retweeted
tweets['Retweeted User'] = retweeted_users

tweets.to_csv('tweets.csv', index = False)
