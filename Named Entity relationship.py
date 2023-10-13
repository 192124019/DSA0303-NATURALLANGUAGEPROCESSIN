import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Get user input
user_input = input("Enter a sentence: ")

# Tokenize the user input into words
words = word_tokenize(user_input)

# Perform part-of-speech tagging
pos_tags = pos_tag(words)

# Perform named entity recognition
named_entities = ne_chunk(pos_tags)

# Function to extract named entities
def extract_entities(tree):
    entities = []
    if hasattr(tree, 'label') and tree.label() is not None:
        entities.append(' '.join([child[0] for child in tree]))
    for child in tree:
        entities.extend(extract_entities(child))
    return entities

# Extract named entities
entities = extract_entities(named_entities)

print("Named Entities:", entities)
