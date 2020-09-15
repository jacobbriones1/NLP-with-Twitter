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
def onehotvector(vocab,word):
    size = len(vocab)
    vector = np.zeros(size,dtype=int)
    #get index of word in list
    if  word.lower() in vocab:
        index = vocab.index(word.lower())
        vector[index]=1
        return vector

#  Creates a list of onehot vectors for a single string
#   using the vocabulary from the entire corpus
def onehotvectors(vocab, string):
    allvectors = []
    print(len(vocab))
    words = word_tokenize(string)
    for word in words:
        if word.lower() in vocab:
            allvectors.append(onehotvector(vocab, word.lower()))
    return allvectors

#  creates all lists of onehot vectors for each string in the  corpus
def all_onehotvectors(corpus):
    allvectors = []
    tokenized = []
    allwords = wordList(corpus)
    Vocab = vocab(allwords)
    for string in corpus:
        allvectors.append(onehotvectors(Vocab,string))
    return allvectors

#  returns the words which are within 'window' distance away from
#   the word in the string.
def wordsNextTo(string, word, window):
    string = str(string)
    string = re.sub(r'[^a-zA-Z ]', '', string)
    print(string)
    words= word_tokenize(string)
    wordlist = []
    for i  in range(len(words)):
        wordlist.append(words[i].lower())
    word = str(word).lower()
    try:
        index = wordlist.index(word)
        print('index of word: ', index)
    except:
        print(word.lower(),' is not in the string')
    
    size = len(wordlist)
    possibleNextTo= []
    if index == 0:ss
        i=1
        while i <=window and i <len(wordlist):
            possibleNextTo.append((wordlist[wordlist.index(word)],wordlist[i]))
            i+=1                

    elif index == len(wordlist)-1:
        i=1
        last=len(wordlist)-1
        while i<= window and len(wordlist)-i>0:
            possibleNextTo.append((wordlist[wordlist.index(word)],wordlist[-i-1]))
            i+=1
    else:
        possibleNextTo=[]
        for i in range(1,window,1):
            if index - i>=0:
                possibleNextTo.append((wordlist[index],wordlist[index-i]))
            if index+i < len(wordlist):
                possibleNextTo.append((wordlist[index],wordlist[index+i]))
                
    return possibleNextTo
