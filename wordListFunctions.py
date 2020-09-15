#  Methods for working with list of texts.

# Written by Jacob Briones

#  For getting a lists of words
from nltk.tokenize import word_tokenize
import numpy as np

# Concatenate corpus into single list of words
#  Note: does not return non-alphabetic tokens
def wordList(corpus):
    wordlist = []
    for words in corpus:
        tokens = word_tokenize(words)
        for word in tokens:
            if word.isalpha()==True:
                wordlist.append(word)
    return wordlist

#  Create vocab from texts
def vocab(wordlist):
    vocab = []
    for word in wordlist:
        if not word.lower() in vocab:
            vocab.append(word.lower())
    return  list(sorted(set(vocab)))


#  Create word frequency dictionary for a list of words
def wordFreq(wordList):
    wordfreq = dict()
    vocab = sorted(set(wordList))
    for word in vocab:
        frequency=0
        for i in range(len(wordList)):
            if wordList[i].lower()==word.lower():
                frequency+=1
        if not word.lower() in wordfreq:
            wordfreq[word.lower()] = frequency
    return wordfreq

# Create onehot vector representation of word
def onehotvector(vocab, word):
    size = len(vocab)
    vector = np.zeros(size,dtype=int)
    #get index of word in list
    if  word.lower() in vocab:
        index = vocab.index(word.lower())
        vector[index]=1
        return vector
    
# create a list of onehot vectors for a some subtexts 
#   from the corpus
def onehotvectors(corpus, string):
    allvectors = []
    wordlist = wordList(corpus)
    Vocab= vocab(corpus)
    words = word_tokenize(string)
    for word in words:
        if word.lower() in Vocab:
            allvectors.append(onehotvector(Vocab, word.lower()))
    return allvectors
