import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sample_text = "I am Apoorv Sethi a Btech student"

tokens = word_tokenize(sample_text)


unigrams = list(ngrams(tokens , 1))
print(unigrams)

bigrams = list(ngrams(tokens , 2))
print(bigrams)

trigrams = list(ngrams(tokens , 3))
print(trigrams)