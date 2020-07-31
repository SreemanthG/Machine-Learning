# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 08:50:06 2020

@author: Admin
"""

import nltk
StopWords = nltk.corpus.stopwords.words('english')

print(len(StopWords))
print(StopWords)



import spacy 
from spacy.lang.en.stop_words import STOP_WORDS

print(len(STOP_WORDS))
print(STOP_WORDS)





import nltk
STOP_WORDS = nltk.corpus.stopwords.words('english')

sentence = "We will go to the movie after the dinner"
print(sentence)

sentence = nltk.tokenize.word_tokenize(sentence)
print(sentence)

notStopWords = [notStopWords for notStopWords in sentence if not notStopWords in STOP_WORDS]
print(notStopWords)

stopWords = [stopWords for stopWords in sentence if stopWords in STOP_WORDS]
print(stopWords)



import spacy
nlp = spacy.load('en_core_web_sm')

sentence = nlp("We will go to movie after the dinner")
print(sentence)

notStopWords = [notStopWords.text for notStopWords in sentence if not notStopWords.is_stop]
print(notStopWords)

stopWords = [stopWords.text for stopWords in sentence if stopWords.is_stop]
print(stopWords)



#Add & Remove a new Stop Word
import nltk
STOP_WORDS = nltk.corpus.stopwords.words('english')
STOP_WORDS.append('Test')

print(len(STOP_WORDS))
print(STOP_WORDS)

import nltk

STOP_WORDS.remove('Test')

print(len(STOP_WORDS))
print(STOP_WORDS)




import spacy
from spacy.lang.en.stop_words import STOP_WORDS

STOP_WORDS.add("Test")

print(len(STOP_WORDS))
print(STOP_WORDS)

import spacy
from spacy.lang.en.stop_words import STOP_WORDS

STOP_WORDS.remove("Test")

print(len(STOP_WORDS))
print(STOP_WORDS)



