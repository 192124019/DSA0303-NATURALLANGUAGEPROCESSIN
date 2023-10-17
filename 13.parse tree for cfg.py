#13Generate a parse tree for a given sentence using a context-free grammar using python program.
import nltk
from nltk import CFG
from nltk.parse.chart import ChartParser

# Define your context-free grammar (CFG)
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the'
    N -> 'cat' | 'dog'
    V -> 'chased'
""")

# Create a ChartParser based on the grammar
parser = ChartParser(grammar)

# Input sentence to parse
sentence = "the cat chased the dog"

# Tokenize the input sentence
tokens = sentence.split()

# Parse the sentence and generate a parse tree
for tree in parser.parse(tokens):
    tree.pretty_print()
