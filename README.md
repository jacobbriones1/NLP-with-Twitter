# NLP with Twitter Data

## About this repository
There are over 330 million twitter users, with over 145 million active users daily. There are on average 6,000
new tweets every second from users all over the world. With twitter being a public platform, this information 
is available to anyone who wants it (within the guidelines of Twitter policy). One of the most valuable uses of 
Twitter data is understanding users' attitude, or *sentiment* towards certain products, 
or events. In hopes of understanding public opinion about some product or event, we can find tweets which contain certain 
*key-words* or *filters* that are relevent to our object of study. And after sifting through this information and extracting
relevant text information, it is possible to determine a relatively accurate model of how  users' view our object of interest.
This kind of analysis is commonly known as **Sentiment Analysis**. Sentiment analysis is one of the most important aspects of 
Natural Language Processing, and a very active area of research. This repository is aimed at studying twitter data using
various types of machine learning techniques, and will also serve as a guide for understanding concepts in Deep Learning and 
Natural Language Processing. <br>
*This Repository is still being developed. For any students or individuals interested in collaborating
or contributing, feel free to contact me at jacobbriones1@gmail.com*<br>
<kbd>
  <img src=trumpWordcloud.png>
</kbd>
### Program Files and Methods:
**getTweets.py** : Is the retrieval program which allows users to access live streaming tweets. The main used in this program is the `tweepy` library,
which is solely used to connect to the Twitter API through python. The user must identify their credentials
in order to connect to the Twitter API. For information on how to access the Twitter API using python see http://docs.tweepy.org/en/latest/ and https://developer.twitter.com/en/docs/getting-started.<br>
#### Methods:
  -  `getTweets([keywords_to_track]) ` : This method must be called to initialize the stream. The input can be any list of
  keywords which the user intends to track. <br>

**credentials.py** : Stores Access and Client information needed to for API authrorization <br>

**cleanTweets.py** : Contains text preprocessing methods used to clean tweet texts. This file is not nearly complere, as it only contains methods for
removing unwanted characters and symbols, and lemmatization. <br>
#### Methods:
  - `cleanTweet(tweet)` : Uses the regex library `re` to remove unwanted characters and symbols which do not provide any meaningful information. Should
  be modified depending on the type of text being processed. See code.<br>
  - `cleanTweets(tweets)` : Applies the `cleanTweet` function to an entire list of tweets. <br>
  - `lemmatize(tweets)` : Lemmatizes list of tweets based on the parts of speech presented by the tweets.<br>

**wordListFunctions.py** : Contains helper methods for analyzing all words contained in a list of tweets. <br>
#### Methods:
  - `wordList([strings])` : Inputs a list of strings, and uses the `nltk.word_tokenize` to convert each string into a list of words.
  I chose not to include non-alphabetic characters in the output, and also converting each word to lowercase.
  The method outputs a single list of lowercase words. <br>
  - `vocab([words])` : inputs a list of words, typically outputted from wordList, and generates a list of all vocabulary words used in the list<br>
  - `wordFreq([words])` : Inputs a list of words of the form outputted by wordList, and returns a dictionary object representing word frequencies.<br>
  - `onehotvector(vocab, word)` : Takes a vocabulary list and a single word as its arguments, and returns the onehot representation of the word. <br>
  - `onehotvectors([strings],[words])` : Takes a list of strings and a list of words as arguments. In terms of tweets, this function inputs a list of
  tweets(not tokenized into words) and a single tweet which has been tokenized into words, and returns a list of onehot vectors for each alphabetic word
  in the tweet<br>
  - `all_onehotvectors(corpus)` : inputs an entire list of strings and returns a list of lists containing onehot vectors <br>
  - `wordsNextTo(string, word, window)` : <br>

**wordPlots.py** : Contains visual tools to analyze word frequency. Needs to include more visual tools.<br>
#### Methods:
  - `wordCloudPlot(dictionary)` : Plots a word cloud. Input parameter should be a word Frequency dictionary. frequency <br>
**word2vec** : Implementation of the Skip-Gram Word2Vec model which does not use pre-trained models. 

## The word2vec functions
The word2vec model allows us to learn *word embeddings* on large pieces of text data. The benefit of using learned word embeddings
is that they allow us to train models without the use of pre-labelled data.In other words, unsupervised learning. These embeddings are
learned using a common machine learning technique: we train a fully connected network with a single hidden layer. <br>

**What exaclty is a Word Embedding?**<br>
A word embedding is a parametrized function which maps words in some language to higher dimensional higher dimensional vector representations.
Intuitively, we can think of an embedded word as a vector which represents the features of the word. Similar words should have similar vectors.
For example, take the sentence: *Kids love eating sugar*. If we choose our embedding space to be 3 dimensional, then the word 'Kids' can be 
represented as something like [1,-1,3]. Now the goal is for similar words to have similar vectors. For example, if we replace the word *Kids* with
the word *Children*, then the three dimensional vector for *Children* could be something like [1,-0.89, 2.9].

<br>
As an example, we can consider the following tweet:<br>
- *If I die from going to a Trump rally, at least Ill die jacked-up on rage, racism, and conspiracy theories.*
<br> 
In order for a computer to process this statement, we need to convert it into a form which it can process. The simplest way to do represent this statement
is to convert each word into a vector known as a **One-Hot Encoded** vector. To convert a word into a One-Hot Encoded vector, the first step is to
create an *ordered* vocabulary list of all *unique* words used in that string. The length of a one-hot encoded vector is the number of unique words in the vocabulary, 
and the entries are  *0* everywhere except for a single *1* in the position of the word in the vocabulary
