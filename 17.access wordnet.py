#17Write program demonstrates how to access WordNet, a lexical database, to retrieve synsets and explore word meanings in python.
import nltk
from nltk.corpus import wordnet

# Download WordNet data (if you haven't already)
nltk.download("wordnet")

# Define a word for which you want to explore meanings
word = "play"

# Get WordNet synsets for the word
synsets = wordnet.synsets(word)

if not synsets:
    print(f"No synsets found for the word '{word}'.")
else:
    for synset in synsets:
        # Get the word's lemma (root form)
        lemma = synset.lemmas()[0].name()
        # Get the word's part of speech (POS)
        pos = synset.pos()
        # Get the definition of the synset
        definition = synset.definition()
        # Get examples of the word's usage
        examples = synset.examples()

        print(f"Lemma: {lemma}")
        print(f"Part of Speech: {pos}")
        print(f"Definition: {definition}")
        if examples:
            print(f"Examples: {', '.join(examples)}")
        print()
