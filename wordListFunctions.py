#  Methods for transforming tokenized tweets into 
#   either a single concatenated list, or a frequency
#   dictionary for a statistical analyis of word
#   frequency.

# Written by Jacob Briones

# Concatenate list of lists of words into single list
def wordList(wordlist):
    allWords = []
    for words in wordlist:
        for word in words:
            allWords.append(word)
    return allWords

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
