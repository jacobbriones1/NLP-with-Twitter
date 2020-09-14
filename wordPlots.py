from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import re

def wordCloudPlot(dictionary):
    wordcloud = WordCloud(background_color='black',
                          max_words=3000,
                          colormap='hsv',
                          relative_scaling=0.5,
                          max_font_size=200,
                          width=2200,
                          height=2200,
                          normalize_plurals=True
                          ).generate_from_frequencies(dictionary)
    # use .generate(space_separated_string) - to generate cloud from text

    plt.figure(figsize=(17,17))
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis('off')
    plt.show()
OnlyAscii = lambda s: re.match('^[\x00-\x7F]+$', s) != None

wf = dict(np.load('wordFrequency.npy',allow_pickle=True).item())
wF = dict()
for i,word in enumerate(wf):
    if OnlyAscii(word)==True:
        wF[word]=i
        
wordCloudPlot(wF)

    
