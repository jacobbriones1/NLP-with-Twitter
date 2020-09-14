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
can reproduce results that aid in understanding user sentiment. <br>
<br>
*--This code uses Python 3.8.5--* <br>

### Program Files and Methods:
`getTweets.py`: Is the retrieval program which allows users to access live streaming tweets. The user must identify their credentials
in order to connect to the Twitter API. For information on how to access the Twitter API using python see http://docs.tweepy.org/en/latest/ 
and https://developer.twitter.com/en/docs/getting-started.

<br>
  -`getTweets([*String* keywords_to_track])`: This method must be called to initialize the stream. The input can be any list of
  keywords which the user intends to track.
<br>



![Biden Word Cloud](bidenWordcloud.png)

![Trump Word Cloud](trumpWordcloud.png)

<p align="center">
  <img src="politicalWordCloud.png" />
</p>
