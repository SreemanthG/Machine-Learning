# -*- coding: utf-8 -*- 
""" 
Created on Thu Jul 23 16:13:45 2020 
 
@author: Sreemanth 
""" 
import re 
from nltk.corpus import stopwords 
 
from nltk.tokenize import word_tokenize 
 
 
with open('Artificaial intelligence.txt', 'r') as file: 
    data = file.read().replace('\n', '') 
     
stop_words = (stopwords.words('english')) 
stop_words.append('a') 
stop_words.append('they') 
stop_words.append('the') 
stop_words.append('his') 
stop_words.append('.') 
stop_words.append(',') 
stop_words.append('so') 
stop_words.append('and') 
stop_words.append('were') 
stop_words.append('from') 
stop_words.append('that') 
stop_words.append('of') 
stop_words.append('in') 
stop_words.append('only') 
stop_words.append('with') 
stop_words.append('to') 
word_tokens = word_tokenize(data) 
 
 
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
 
print(len(filtered_sentence)) 
 
f1 = filtered_sentence 
### Frequecy - 1 
frequency = {} 
for word in filtered_sentence: 
    count = frequency.get(word,0) 
    frequency[word] = count + 1 
frequency_list = frequency.keys() 
  
for words in frequency_list: 
    print (words, frequency[words]) 
 
 
with open('machine learning.txt', 'r') as file: 
    data = file.read().replace('\n', '') 
 
 
word_tokens = word_tokenize(data) 
 
##print(word_tokens) 
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
 
print(len(filtered_sentence)) 
 
f2 = filtered_sentence 
 
### Frequecy - 2 
frequency = {} 
for word in filtered_sentence: 
    count = frequency.get(word,0) 
    frequency[word] = count + 1 
frequency_list = frequency.keys() 
  
for words in frequency_list: 
    print (words, frequency[words]) 
     
     
#Group in a list the words common for two text files and show their total count 
 
if len(f1) != 0 | len(f2) != 0: 
    for words in f1: 
        for wordds in f2: 
            if words == wordds: 
                print(words) 