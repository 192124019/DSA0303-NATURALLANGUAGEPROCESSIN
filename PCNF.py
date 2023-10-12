import nltk
from nltk import CFG, PCFG
from nltk.parse import ViterbiParser

# Define a PCFG
pcfg_grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.7] | N [0.3]
    VP -> V [0.4] | V NP [0.6]
    Det -> 'the' [1.0]
    N -> 'cat' [0.5] | 'dog' [0.5]
    V -> 'chased' [0.7] | 'saw' [0.3]
""")

# Create a parser with the PCFG
parser = ViterbiParser(pcfg_grammar)

# Input sentence
sentence = "the cat chased the dog"

# Tokenize the input
tokens = nltk.word_tokenize(sentence)

# Parse the sentence
for tree in parser.parse(tokens):
    tree.pretty_print()
