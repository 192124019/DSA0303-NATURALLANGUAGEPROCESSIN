import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')  # Download the WordNet data

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Get user input
user_input = input("Enter a sentence: ")

# Tokenize the user input into words
words = nltk.word_tokenize(user_input)

# Lemmatize the words
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# Join the lemmatized words back into a sentence
lemmatized_sentence = ' '.join(lemmatized_words)

print("Original Input:", user_input)
print("Lemmatized Sentence:", lemmatized_sentence)
