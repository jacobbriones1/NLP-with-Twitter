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
Natural Language Processing, and a very active area of research. This repository is aimed at understanding the sentiment 
of some of the topics which are trending on Twitter<br>

<kbd>
  <img src=trumpWordcloud.png>
</kbd>

## Getting Tweets:
To get tweets, download the `get_tweets.py` file, and define a CustomStreamListener object, and use the `collect` method as follows:
```
dir = 'C:path\\to\\directory\\containing\\credentials\\file'
csl = CustomStreamListener(file_path=dir)
csl.collect(['joe biden','donald trump'])
```
The dir should contain a file called `credentials.py` which should define the following:
```
CONSUMER_KEY = "cyDpsp0O**************"
CONSUMER_SECRET = "rMoOg**************"
ACCESS_TOKEN = "13040287**************"
ACCESS_SECRET = "hByQaKO**************"
```
For instructions on how to get authentication credentials, check out [Twitter's tutorials](https://developer.twitter.com/en/docs/getting-started).
This should begin streaming tweets, which you will be able to view in the command prompt
![Collecting Tweets](https://user-images.githubusercontent.com/70331998/121632815-8ac2d080-ca36-11eb-849b-f786332c8245.png)

### Repository Files:
**get_tweets.py** : Is the file which contains objects which allow users to access live streaming tweets. The main library used in this program is the `tweepy` library,
which is solely used to connect to the Twitter API through python. The user must identify their credentials
in order to connect to the Twitter API. For information on how to access the Twitter API using python see http://docs.tweepy.org/en/latest/ and https://developer.twitter.com/en/docs/getting-started.<br>


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

