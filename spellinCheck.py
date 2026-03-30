from textblob import TextBlob

text = "Hi  I am learming AI"

blob = TextBlob(text)

corrected_text = blob.correct()

print("original :"  , text)
print("corrected : " , corrected_text)
