# processTweets.py is the main program used to clean our 
#  text data. There are three methods. The cleanTweet method
#  is used to simplify the cleanTweets method. These methods
#  use the regex library re to remove unwanted symbols and
#  transform the data into a form which is easier to process.

#  !!! A method for stemming should be added as well as any other
#        methods for preprocessing data !!!!!!

# Written by Jacob Briones

import nltk
from nltk import word_tokenize,sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import re
import numpy as np
import string

# Function to clean tweets
def cleanTweet(tweet):
    # Remove HTML special entities (e.g. &amp;)
    tweet = re.sub(r'\&\w*;', '', tweet)
    
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','',tweet)
    
    # Remove tickers
    tweet = re.sub(r'\$\w*', '', tweet)
    
    # To lowercase
    tweet = tweet.lower()
    
    # Remove hyperlinks
    tweet = re.sub(r'https?:\/\/.*\/\w*', '', tweet)
    
    # Remove hashtags
    tweet = re.sub(r'#\w*', '', tweet)
    
    # Remove Punctuation and split 's, 't, 've with a space for filter
    tweet = re.sub(r'[' + string.punctuation.replace('@', '') + ']+', ' ', tweet)
    
    # Remove words with 2 or fewer letters
    tweet = re.sub(r'\b\w{1,2}\b', '', tweet)
    
    # Remove whitespace (including new line characters)
    tweet = re.sub(r'\s\s+', ' ', tweet)
    
    # Remove single space remaining at the front of the tweet.
    tweet = tweet.lstrip(' ')
    
    # Remove characters beyond Basic Multilingual Plane (BMP) of Unicode:
    tweet = ''.join(c for c in tweet if c <= '\uFFFF')
    
    return tweet

#  Function which returns a list of cleaned tweets
def cleanTweets(tweets):
    cleaned = []

    for tweet in tweets:
        cleaned.append(cleanTweet(tweet))
    return cleaned

#  Function which returns a list of lemmatized sentences
#    where each sentence is a list of words which have been
#    simplified using the WordNetLemmatizer.
def lemmatize(tweets):
    # Arrray to store tokenized sentences
    sentences = []

    for i in range(len(tweets)):
        # Sentence tokenization
        tweet = sent_tokenize(tweets[i])
        sentences.append(tweet)

    # Array to store tokenized words
    words = []

    for sentence in sentences:
        # Word tokenization
        for Words in sentence:
            words.append(word_tokenize(Words))

    #  Get the part of speech
    def get_wordnet_pos(treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return ''

    #  Lemmatize 
    lemmatizer = WordNetLemmatizer()
    lemmatizedWords = []
    
    for i in range(len(words)):
        words2append = []
        treebanktags=nltk.pos_tag(words[i])
        for j in range(len(treebanktags)):
            if get_wordnet_pos(treebanktags[j][1])!= '':
                words2append.append(lemmatizer.lemmatize(treebanktags[j][0],get_wordnet_pos(treebanktags[j][1])))
        lemmatizedWords.append(words2append)

    return lemmatizedWords
