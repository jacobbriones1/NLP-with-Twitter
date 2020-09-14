# Analyzing-Twitter-Data

## What is this repository useful for?
There are over 330 million twitter users, with over 145 million active users daily. There are on average 6,000
new tweets every second from users all over the world. With twitter being a public platform, this information 
is available to anyone who wants it (within the guidelines of Twitter policy). <br>
One of the most valuable uses of Twitter data is understanding users' attitude, or *sentiment* towards certain products, 
or events. In hopes of understanding public opinion about some product or event, we can find tweets which contain certain 
*key-words* or *filters* that are relevent to our object of study. And after sifting through this information and extracting
relevant text information, it is possible to determine a relatively accurate model of how  users' view our object of interest.
This kind of analysis is commonly known as **Sentiment Analysis**. This repository is aimed at contributing software which
can reproduce results that aid in understanding user sentiment, and also developing new research in machine learning. <br>
<br>
*--This code uses Python 3.8.5--* <br>
![Words Associated to Trump](trumpWordcloud.png)

### Program Files and Methods:
`getTweets.py`: Is the retrieval program which allows users to access live streaming tweets. The main used in this program is the `tweepy` library,
which is solely used to connect to the Twitter API through python. The user must identify their credentials
in order to connect to the Twitter API. For information on how to access the Twitter API using python see http://docs.tweepy.org/en/latest/ and https://developer.twitter.com/en/docs/getting-started.<br>
#### Methods:
  -  `getTweets([keywords_to_track]) ` : This method must be called to initialize the stream. The input can be any list of
  keywords which the user intends to track. <br>

`credentials.py` : Stores Access and Client information needed to for API authrorization <br>

`cleanTweets.py` : Contains text preprocessing methods used to clean tweet texts. This file is not nearly complere, as it only contains methods for
removing unwanted characters and symbols, and lemmatization. <br>
#### Methods:
  - `cleanTweet(tweet)` : Uses the regex library `re` to remove unwanted characters and symbols which do not provide any meaningful information. Should
  be modified depending on the type of text being processed. See code.<br>
  - `cleanTweets(tweets)` : Applies the `cleanTweet` function to an entire list of tweets. <br>
  - `lemmatize(tweets)` : Lemmatizes list of tweets based on the parts of speech presented by the tweets.<br>

`wordListFunctions.py` : Contains helper methods for analyzing all words contained in a list of tweets. <br>
#### Methods:
  - `wordList(wordlist)` : Input is a list of tweets tokenized into words:`tweet: ['a tweet'] ---> wordList: [['a'],['tweet']]`.
  The method outputs a single list, where each entry is a word rather than another list. <br>
  - `wordFreq(wordList)` : Inputs a list of words of the form outputted by wordList, and returns a dictionary object representing word frequencies.

`wordPlots` : Contains visual tools to analyze word frequency. Needs to include more visual tools.<br>
#### Methods:
  - `wordCloudPlot(dictionary)` : Plots a word cloud. Input parameter should be a word Frequency dictionary. frequency <br>
  
`processMyTweets` <br>
