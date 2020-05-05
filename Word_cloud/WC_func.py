#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 13:15:33 2020

@author: ender
"""
#Program to create word cloud of abundance data
#Pre-requisits: csv file named Word_cloud.csv, two columns ID for species
#                                                          AB for abundances
#


import pandas as pd
import matplotlib.pyplot as plt 
from wordcloud import WordCloud
import sys


data = sys.argv[1]

data = pd.read_csv("Word_cloud.csv", decimal=".")
   

data.set_index('ID',inplace=True)
total_ab = data["AB"].sum()
total_ab

max_words = 1000
word_string = ''
for ID in data.index.values:
    # check if country's name is a single-word name
    if len(ID.split(' ')) == 1:
        repeat_num_times = int(data.loc[ID, 'AB']/float(total_ab)*max_words)
        word_string = word_string + ((ID + ' ') * repeat_num_times)
        
                             
# display the generated text
word_string

# create the word cloud
wordcloud = WordCloud(background_color='black',collocations=False).generate(word_string)


fig = plt.figure()
fig.set_figwidth(14)
fig.set_figheight(18)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('WC.png')
