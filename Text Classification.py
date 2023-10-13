from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import numpy as np

# Sample data for sentiment analysis
corpus = [
    ("I love this product.", "positive"),
    ("Terrible customer service.", "negative"),
    ("It's okay, nothing special.", "neutral"),
    # Add more data and categories as needed
]

# Extract text and labels
texts, labels = zip(*corpus)

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Transform the text data into TF-IDF features
X = tfidf_vectorizer.fit_transform(texts)

# Initialize a Naive Bayes classifier
classifier = MultinomialNB()

# Train the classifier
classifier.fit(X, labels)

# Get user input
user_input = input("Enter a sentence for sentiment analysis: ")

# Transform the user input into TF-IDF features
user_input_tfidf = tfidf_vectorizer.transform([user_input])

# Predict the sentiment class
predicted_class = classifier.predict(user_input_tfidf)

print("Predicted Sentiment:", predicted_class[0])
