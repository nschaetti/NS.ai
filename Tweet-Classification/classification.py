#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Imports
import json
import codecs
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

# Open file
dataset = json.load(codecs.open(u"dataset.json", 'rb', encoding='utf-8'))

# Count vector
count_vec = CountVectorizer(ngram_range=(1, 1))

# TF-IDF transformer
tfidf_transformer = TfidfTransformer()

# Classifier
classifier = MultinomialNB()

# Pipleline
text_clf = Pipeline([('vec', count_vec),
                     ('tfidf', tfidf_transformer),
                     ('clf', classifier)])

# Training et evaluation
scores = cross_val_score(text_clf, dataset['X'], dataset['Y'], cv=10)

# Show evaluation
print(scores)

# Train on entire dataset
text_clf.fit(dataset['X'], dataset['Y'])

# For each users
for index, user in enumerate(dataset['test_name']):
    print(u"Trying {}".format(user))

    # Predict
    prediction = text_clf.predict([dataset['test_X'][index]])

    # Print prediction
    print(u"{} is predicted as {}".format(user, prediction))
# end for
