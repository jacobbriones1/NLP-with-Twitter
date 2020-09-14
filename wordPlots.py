# Plot methods for analyzing text. 
#   !!!  More plot methods should be added for better analysis  !!!

# Written by Jacob Briones 

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import re

#  Return a word cloud. The input should be a word frequency
#   dictionary, which the wordFreq method computes in the 
#   wordListFunctions.py file.

def wordCloudPlot(dictionary):
    wordcloud = WordCloud(background_color='black',
                          max_words=150,
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
    
