from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# reviews = ['This movie was fantastic! A must-watch.',
#            'I didn\'t enjoy this movie at all.',
#            'Amazing storyline and great acting!',
#            'The plot was dull and predictable.',
#            'Loved the cinematography! Highly recommended.']

# labels = ['positive', 'negative', 'positive', 'negative', 'positive']
reviews = [
# Positive
"This movie was fantastic and inspiring!",
"I absolutely loved the storyline.",
"Amazing acting and great direction.",
"One of the best movies I have ever seen.",
"Brilliant performance by the cast.",
"Loved every moment of this film.",
"Highly recommended for everyone.",
"Outstanding cinematography and music.",
"A masterpiece, truly शानदार!",
"The plot was engaging and emotional.",
"Superb execution and great visuals.",
"Heartwarming and beautifully made.",
"Excellent script and acting.",
"This film exceeded my expectations.",
"A must-watch for movie lovers.",
"Great movie with a powerful message.",
"I enjoyed this movie a lot.",
"Fantastic experience watching this.",
"Very entertaining and well-made.",
"Loved the characters and story.",

# Negative
"This movie was boring and slow.",
"I did not enjoy the film at all.",
"Worst movie I have ever seen.",
"The plot was weak and predictable.",
"Terrible acting and poor direction.",
"I regret watching this movie.",
"Not worth my time.",
"Very disappointing experience.",
"The storyline was confusing.",
"Bad editing and weak screenplay.",
"Completely waste of time.",
"I expected more from this film.",
"The movie was too long and dull.",
"Poor character development.",
"Nothing interesting in the movie.",
"Very low-quality production.",
"The acting was terrible.",
"Uninteresting and boring movie.",
"I would not recommend this.",
"This movie failed to impress me.",

# Neutral / Mixed
"The movie was okay, not great.",
"It had some good and bad parts.",
"Average movie with decent acting.",
"Not bad but not amazing either.",
"Some scenes were good, others were dull.",
"It was a one-time watch.",
"The film was fine overall.",
"Nothing special but okay.",
"Decent movie but forgettable.",
"Moderately entertaining."
]

labels = [
# Positive (20)
"positive","positive","positive","positive","positive",
"positive","positive","positive","positive","positive",
"positive","positive","positive","positive","positive",
"positive","positive","positive","positive","positive",

# Negative (20)
"negative","negative","negative","negative","negative",
"negative","negative","negative","negative","negative",
"negative","negative","negative","negative","negative",
"negative","negative","negative","negative","negative",

# Neutral (10)
"neutral","neutral","neutral","neutral","neutral",
"neutral","neutral","neutral","neutral","neutral"
]
#creating vectors
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(reviews)

#spliting data
x_train , x_test , y_train , y_test = train_test_split(x , labels , test_size=0.2 , random_state=42)

#training model
model = MultinomialNB()
model.fit(x_train , y_train)

#test the model
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

print('Accuracy:', accuracy)

#checking 
if(accuracy > 0.8):
    print("movie worth watching")
else:
    print("not worth watchin")