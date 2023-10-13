import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')  # Download the stop words data

# Get user input
user_input = input("Enter a sentence: ")

# Tokenize the user input into words
words = nltk.word_tokenize(user_input)

# Get the list of English stop words
stop_words = set(stopwords.words('english'))

# Remove stop words from the input
filtered_words = [word for word in words if word.lower() not in stop_words]

# Join the filtered words back into a sentence
filtered_sentence = ' '.join(filtered_words)

print("Original Input:", user_input)
print("Filtered Sentence:", filtered_sentence)
