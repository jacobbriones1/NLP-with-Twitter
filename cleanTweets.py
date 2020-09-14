import nltk
from nltk import word_tokenize,sent_tokenize
from nltk.tokenize import TreebankWordTokenizer
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
    
    # Remove hyperlinks
    tweet = re.sub(r'https?:\/\/.*\/\w*', '', tweet)
    
    # Remove hashtags
    tweet = re.sub(r'#\w*', '', tweet)
    
    # Remove whitespace (including new line characters)
    tweet = re.sub(r'\s\s+', ' ', tweet)
    
    # Remove single space remaining at the front of the tweet.
    tweet = tweet.lstrip(' ')
    
    return tweet

#  Function which returns a list of cleaned tweets
def cleanTweets(tweets):
    print('Cleaning tweets...')
    cleaned = []

    for tweet in tweets:
        cleaned.append(cleanTweet(tweet))
    return cleaned

#  Function which returns a list of lemmatized sentences
#    where each sentence is a list of words which have been
#    simplified using the WordNetLemmatizer.
def lemmatize(tweets):
    print('Beginning lemmatization...')
    # Arrray to store tokenized sentences
    
    # Array to store tokenized words
    words = []
    tokenizer = TreebankWordTokenizer()
    for tweet in tweets:
        words.append(tokenizer.tokenize(tweet))
    print(len(tweets), ' tweets--->',len(words),' words')

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

    #  Lemmatize words
    lemmatizer = WordNetLemmatizer()
    lemmatizedWords = []

    for i in range(len(words)):
        words2append = []
        treebanktags=nltk.pos_tag(words[i])
        for j in range(len(treebanktags)):
            if get_wordnet_pos(treebanktags[j][1]) != '':
                words2append.append(lemmatizer.lemmatize(treebanktags[j][0],get_wordnet_pos(treebanktags[j][1])))
        lemmatizedWords.append(words2append)

    for i in range(len(lemmatizedWords)):
        lemmatizedWords[i][:]=[word for word in lemmatizedWords[i] if not word in {'RT','rt','//t','http','='}]

    for words in lemmatizedWords:
        if len(words)==1:
            lemmatizedWords.remove(words)

    return lemmatizedWords

