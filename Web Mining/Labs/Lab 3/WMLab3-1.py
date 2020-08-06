import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer 

stop_words = set(stopwords.words('english'))

ps = PorterStemmer()
lemmatizer = WordNetLemmatizer() 

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
for w in example_words:
    print(ps.stem(w), " - ", lemmatizer.lemmatize(w))


new_text = "It is important to by very pythonly while you are pythoning with python. \\\
            All pythoners have pythoned poorly at least once."
words = word_tokenize(new_text)

tagged = nltk.pos_tag(words) 


for w in words:
    print(w, " - ", ps.stem(w), " - ", lemmatizer.lemmatize(w))

print(tagged) 




from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer(language='english')

tokens = ["python","pythoner","pythoning","pythoned","pythonly"]

for token in tokens:
    print(token + ' --> ' + stemmer.stem(token))




import spacy
sp = spacy.load('en_core_web_sm')
sentence7 = sp(u'A letter has been written, asking him to be released')

for word in sentence7:
    print(word.text + '  ===>', word.lemma_)









from nltk.corpus import wordnet 

example_sent = "sample sentence showing off the stop words filtration"

words = word_tokenize(example_sent)

words = [w for w in words if not w in stop_words] 


for w in words:
    syns = wordnet.synsets(w) 
    print(w, " - ", syns) 


for w in words:
    syn = wordnet.synsets(w)
    print("\n\n",w,"\n")
    print('Word and Type : ' + syn[0].name())
    print('Synonym : ' + syn[0].lemmas()[0].name())
    print('The meaning : ' + syn[0].definition())
    print('Example : ' + str(syn[0].examples())) 


synonyms = []

for w in words:
    for syn in wordnet.synsets(w):
        for lm in syn.lemmas():
            synonyms.append(lm.name())#adding into synonyms
    print(w,"----",synonyms,"\n\n")
    synonyms = []


antonyms = []

for w in words:
    for syn in wordnet.synsets(w):
        for lm in syn.lemmas():
            if lm.antonyms():
                antonyms.append(lm.antonyms()[0].name())#adding into antonyms
    print(w,"----",antonyms,"\n\n")
    antonyms = []