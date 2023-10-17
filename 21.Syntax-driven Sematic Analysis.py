#21. Create a python program that performs syntax-driven semantic analysis by extracting noun phrases and their meanings from a sentence.

import spacy

# Load the pre-trained model
nlp = spacy.load("en_core_web_sm")

# Get user input
sentence = input("Enter a sentence: ")  #The quick brown fox jumped over the lazy dog.

# Process the input sentence with SpaCy
doc = nlp(sentence)

# Extract noun phrases and their meanings
noun_phrases = []
for chunk in doc.noun_chunks:
    noun_phrase = chunk.text
    meanings = [token.text for token in chunk.root.subtree]
    noun_phrases.append((noun_phrase, " ".join(meanings)))

# Display the extracted noun phrases and their meanings
print("Noun Phrases and Their Meanings:")
for noun_phrase, meaning in noun_phrases:
    print(f"Noun Phrase: {noun_phrase}")
    print(f"Meaning: {meaning}")
    print()
