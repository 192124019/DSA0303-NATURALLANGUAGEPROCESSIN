#14.Create a program in python to check for agreement in sentences based on a context-free grammar&#39;s rules.
import nltk
from nltk import CFG, ChartParser

nltk.download("punkt")

# Define a context-free grammar for subject-verb agreement
grammar = CFG.fromstring("""
    S -> NP_SG VP_SG | NP_PL VP_PL
    NP_SG -> Det_SG N_SG
    NP_PL -> Det_PL N_PL
    VP_SG -> V_SG
    VP_PL -> V_PL
    Det_SG -> 'the' | 'a'
    Det_PL -> 'the'
    N_SG -> 'cat' | 'dog'
    N_PL -> 'cats' | 'dogs'
    V_SG -> 'chases' | 'barks'
    V_PL -> 'chase' | 'bark'
""")

def check_agreement(sentence):
    parser = ChartParser(grammar)
    tokens = nltk.word_tokenize(sentence.lower())  # Tokenize and convert to lowercase for simplicity

    for tree in parser.parse(tokens):
        return True  # If a parse tree is found, there is agreement
    return False

# Get user input 
user_sentence = input("Enter a sentence: ") #the cat chases

if check_agreement(user_sentence):
    print("The sentence has subject-verb agreement.")
else:
    print("The sentence lacks subject-verb agreement.")
