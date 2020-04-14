# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:53:39 2020

@author: Novin
"""
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

corpus = '''If two items to be compared are themselves sequences of the same type, the lexicographical comparison
 is carried out recursively. If all items of two sequences compare equal, the sequences are considered equal'''

stopwords = ['to','the','of','be','out']

words = []
keywords = []
sentences = corpus.split('.')

for sen in sentences:
    temp = sen.strip().split(' ')
    for w in temp:
        if w not in stopwords:
            words.append(w)

print(words)

print('===============================')

keywords = set(words)
print(keywords)

print('===============================')

TFIDF = {}

for word in words:
        if word in TFIDF:
            TFIDF[word] += 1
        else:
            TFIDF[word] = 1
    
print(TFIDF)

print('===============================')

wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(corpus)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
        

    
    

