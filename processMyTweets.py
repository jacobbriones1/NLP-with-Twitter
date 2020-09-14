#  Example case: analyzing sentiment towards Politidal Candidates:

import numpy as np
import pandas as pd
from processTweets import cleanTweets, lemmatize
from wordListFunctions import wordList,wordFreq
from wordPlots import 
import nltk
import matplotlib.pyplot as plt
from wordcloud import wordCloudPlot
from collections import Counter

data = pd.read_csv("tweets.csv")
tweets = data.Text
hashtags= data.Hashtags
trumpTweets = []
bidenTweets = []

#  Separate tweets: tweets containing only trump, and tweets containing only biden.
for i in range(len(tweets)):
    if ('trump' in tweets[i].lower() or 'trump' in str(hashtags[i]).lower()) and  (not 'biden' in tweets[i].lower() or not 'biden' in str(hashtags[i]).lower()):
        trumpTweets.append(tweets[i])

    elif (not 'trump' in tweets[i].lower() or not 'trump' in str(hashtags[i]).lower()) and  ('biden' in tweets[i].lower() or 'biden' in str(hashtags[i]).lower()):
        bidenTweets.append(tweets[i])

# Preprocess tweets:

# Reformat and remove unwanted characters:
trump = cleanTweets(trumpTweets)
biden = cleanTweets(bidenTweets)

# Lemmatize
trump = lemmatize(trump)
biden = lemmatize(biden)

# concatenate lists into single list 
trumpWords = wordList(trump)
bidenWords = wordList(biden)

# get word frequencies
trumpFreq = wordFreq(trumpWords)
bidenFreq = wordFreq(bidenWords)

# plot the word clouds
wordCloudPlot(trumpFreq)
wordCloudPlot(bidenFreq)
