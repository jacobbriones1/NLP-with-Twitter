  
#  The tweets2csv.py program takes the tweets.json file created by the getTweets.py function
#   and returns a csv named tweets.csv containing the relevant information which we will
#   be processed.
#   Written by Jacob Briones

import json
from datetime import datetime as dt
import pandas as pd
import re

def json_to_csv(file_path):
    #  Set file path
    tweets_data_path = file_path
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
    
    tweets['created_at'] =  list(map(lambda tweet: str(tweet['created_at']), tweets_data))
    tweets['id'] = list(map(lambda tweet: tweet['id'], tweets_data))
    tweets['id_str'] = list(map(lambda tweet: tweet['id_str'], tweets_data))
    tweets['source'] = list(map(lambda tweet: tweet['source'], tweets_data))
    tweets['user'] = list(map(lambda tweet: tweet['user'], tweets_data))
    tweets['retweet_count'] = list(map(lambda tweet: tweet['retweet_count'], tweets_data))
    tweets['retweeted'] = list(map(lambda tweet: tweet['retweeted'], tweets_data))
    
    in_reply_to_status_id = []
    in_reply_to_status_id_str = []
    in_reply_to_user_id = []
    in_reply_to_user_id_str = []
    in_reply_to_screen_name = []
    coordinates = []
    place = []
    text = []
    is_quote_status = []
    quoted_status_id = []
    quoted_status_id_str = []
    retweeted_status = []
    favorite_count = []
    entities = []
    extended_entities = []
    favorited = []
    retweeted = []
    
    for tweet in tweets_data:
        if 'in_reply_to_status_id' in tweet:
            in_reply_to_status_id.append(tweet['in_reply_to_status_id'])
            in_reply_to_status_id_str.append(tweet['in_reply_to_status_id_str'])
        else:
            in_reply_to_status_id.append(None)
            in_reply_to_status_id_str.append(None)
            
        if 'in_reply_to_user_id' in tweet:
            in_reply_to_user_id.append(tweet['in_reply_to_user_id'])
            in_reply_to_user_id_str.append(tweet['in_reply_to_user_id_str'])
        else:
            in_reply_to_user_id.append(None)
            in_reply_to_user_id_str.append(None)
                    
        if 'in_reply_to_screen_name' in tweet:
            in_reply_to_screen_name.append(tweet['in_reply_to_screen_name'])
        else:
            in_reply_to_screen_name.append(None)
        
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
                    
        elif tweet['truncated'] == True and tweet['is_quote_status']==False \
            and not 'retweeted_status' in tweet:
            text.append(tweet['extended_tweet']['full_text'])
            
        else:
            text.append(tweet['text'])
        
        if 'coordinates' in tweet:
            coordinates.append(tweet['coordinates'])
        else:
            coordinates.append(None)
        
        if 'place' in tweet:
            place.append(tweet['place'])
        else:
            place.append(None)
        
        if tweet['is_quote_status']==True:
            is_quote_status.append('True')
            quoted_status_id.append(tweet['quoted_status_id'])
            quoted_status_id_str.append(tweet['quoted_status_id_str'])
        else:
            is_quote_status.append('False')
            quoted_status_id.append(None)
            quoted_status_id_str.append(None)
        
        if 'retweeted_status' in tweet:
            retweeted_status.append(tweet['retweeted_status'])
        else:
            retweeted_status.append(None)
        
        if 'favorite_count' in tweet:
            favorite_count.append(tweet['favorite_count'])
        else:
            favorite_count.append(0)
        
        if 'entities' in tweet:
            entities.append(entities)
        else:
            entities.append(None)
        
        if 'extended_entities' in tweet:
            extended_entities.append(tweet['extended_entities'])
        else:
            extended_entities.append(None)
        
        if 'favorited' in tweet:
            favorited.append(tweet['favorited'])
        else:
            favorited.append(tweet['favorited'])
        
    tweets['in_reply_to_status_id'] = in_reply_to_status_id
    tweets['in_reply_to_status_id_str'] = in_reply_to_status_id_str
    tweets['in_reply_to_user_id'] = in_reply_to_user_id
    tweets['in_reply_to_user_id_str'] = in_reply_to_user_id_str
    tweets['in_reply_to_screen_name'] = in_reply_to_screen_name
    tweets['text'] = text
    tweets['coordinates'] = coordinates
    tweets['place'] = place
    tweets['is_quote_status'] = is_quote_status
    tweets['quoted_status_id'] = quoted_status_id
    tweets['quoted_status_id_str'] = quoted_status_id_str
    tweets['retweeted_status'] = retweeted_status
    tweets['favorite_count'] = favorite_count
    tweets['entities'] = entities
    tweets['extended_entities'] = extended_entities
    tweets['favorited'] = favorited
    
    tweets.to_csv(dt.today().strftime('%Y-%m-%d-tweets.csv'), index = False)
