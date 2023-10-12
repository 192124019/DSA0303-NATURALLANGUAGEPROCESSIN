import nltk
from nltk.grammar import CFG

# Define a context-free grammar (CFG)
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the'
    N -> 'cat' | 'dog'
    V -> 'chased' | 'ate'
""")

# Create an Earley parser
earley_parser = nltk.EarleyChartParser(grammar)

# Get user input for a sentence
user_input = input("Enter a sentence: ")

# Tokenize the input
words = user_input.split()

# Parse the input
parsed = False
for tree in earley_parser.parse(words):
    tree.pretty_print()
    parsed = True

if not parsed:
    print("The sentence couldn't be parsed with the given grammar.")
