#part Of Speech
import nltk

# Download NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Get user input
user_input = input("Enter a sentence: ")

# Tokenize the input sentence
words = nltk.word_tokenize(user_input)

# Use NLTK's part-of-speech tagging
pos_tags = nltk.pos_tag(words)

print("Parts of Speech:")
for word, pos in pos_tags:
    print(f"{word}: {pos}")
