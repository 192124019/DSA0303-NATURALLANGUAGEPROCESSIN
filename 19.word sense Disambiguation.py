#19.Create a program for word sense disambiguation using the Lesk algorithm using python.
import nltk
from nltk.corpus import wordnet
from nltk.wsd import lesk

# Download necessary resources if not already downloaded
nltk.download('punkt')

# Get a sentence input from the user
sentence = input("Enter a sentence: ") #I went to the bank to deposit some money.

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Perform word sense disambiguation
for word in tokens:
    synset = lesk(tokens, word)
    if synset:
        print(f"Word: {word}, Sense: {synset.name()}, Definition: {synset.definition()}")
    else:
        print(f"No sense found for '{word}'")
