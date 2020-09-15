#  Methods for working with list of texts.

# Written by Jacob Briones

#  For getting a lists of words
from nltk.tokenize import word_tokenize

# Concatenate list of lists of words into single list
def wordList(tweetlist):
    words = []
    for tweet in tweetlist:
        tokens = word_tokenize(tweet)
        for word in tokens:
            if word.isalpha()==True:
                words.append(word)
    return words


#  Create word frequency dictionary
def wordFreq(wordList):
    vocab = sorted(set(wordList))
    wordfreq = dict()
    for word in vocab:
        frequency=0
        for i in range(len(wordList)):
            if wordList[i].lower()==word.lower():
                frequency+=1
        if not word.lower() in wordfreq:
            wordfreq[word.lower()] = frequency
    return wordfreq

#  Create a list of all words used in texts.
def vocab(wordlist):
    vocab = []
    for word in wordlist:
        if not word in vocab:
            vocab.append(word)
    return list(sorted(set(vocab)))
