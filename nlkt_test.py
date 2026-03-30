import nltk
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize

sample_text = "I am a GenAI learner"
tokens = word_tokenize(sample_text)

print("tokens:", tokens)