import numpy as np
import pandas as pd
from processTweets import cleanTweets, lemmatize, wordList, wordFreq
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

data = pd.read_csv("twitter_trump_biden.csv")
tweets = data.Text
hashtags= data.Hashtags
trumpTweets = []
bidenTweets = []
trumpAndbidenTweets = []

for i in range(len(tweets)):
    if ('trump' in tweets[i].lower() or 'trump' in str(hashtags[i]).lower()) and  (not 'biden' in tweets[i].lower() or not 'biden' in str(hashtags[i]).lower()):
        trumpTweets.append(tweets[i])

    elif (not 'trump' in tweets[i].lower() or not 'trump' in str(hashtags[i]).lower()) and  ('biden' in tweets[i].lower() or 'biden' in str(hashtags[i]).lower()):
        bidenTweets.append(tweets[i])
        
    elif ('trump' in tweets[i].lower() or 'trump' in str(hashtags[i]).lower()) or ('biden' in tweets[i].lower() or 'biden' in str(hashtags[i]).lower()):
        trumpAndbidenTweets.append(tweets[i])

trump = cleanTweets(trumpTweets)
biden = cleanTweets(bidenTweets)
trumpbiden = cleanTweets(trumpAndbidenTweets)

trump = lemmatize(trump)
biden = lemmatize(biden)
trumpbiden = lemmatize(trumpbiden)

trumpWords = wordList(trump)
trumpFreq = wordFreq(trumpWords)

bidenWords = wordList(biden)
bidenFreq = wordFreq(bidenWords)

bothWords = wordList(trumpbiden)
bothFreq = wordFreq(bothWords)
        
ytrump, ybiden, yboth = [],[],[]

for i in range(len(trumpFreq)):
    ytrump=trumpFreq[i][0]
for i in range(len(bidenFreq)):
    ybiden = bidenFreq[i][0]
    


wordcloud = WordCloud(width=900,
                      height=500,
                      max_words=500,
                      max_font_size=100,
                      relative_scaling=0.5,
                      colormap='Blues',
                      normalize_plurals=True).generate_from_frequencies(Counter(trumpWords))
plt.figure(figsize=(17,14))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

wordcloud = WordCloud(width=900,
                      height=500,
                      max_words=500,
                      max_font_size=100,
                      relative_scaling=0.5,
                      colormap='Blues',
                      normalize_plurals=True).generate_from_frequencies(Counter(bidenWords))
plt.figure(figsize=(17,14))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

