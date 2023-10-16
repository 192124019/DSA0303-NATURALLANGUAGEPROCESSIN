
#3Write program demonstrates how to perform morphological analysis using the NLTK library in py
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def morphological_analysis(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)

    # Initialize the Porter Stemmer
    stemmer = PorterStemmer()

    # Perform morphological analysis for each word in the sentence
    for word in words:
        # Perform stemming using the Porter Stemmer
        stem = stemmer.stem(word)

        # Get the part-of-speech tag for the word
        pos_tag = nltk.pos_tag([word])[0][1]

        # Get the WordNet synsets for the word
        synsets = wordnet.synsets(word)

        print(f"Word: {word}")
        print(f"Stem: {stem}")
        print(f"Part of Speech: {pos_tag}")
        
        if synsets:
            # Print the first WordNet synset for the word
            print(f"First WordNet Synset: {synsets[0].name()}")
            print(f"Definition: {synsets[0].definition()}")
            print(f"Examples: {synsets[0].examples()}\n")
        else:
            print("No WordNet Synsets found for this word.\n")

if __name__ == "__main__":
    user_input = input("Enter a sentence for morphological analysis: ")
    morphological_analysis(user_input)
