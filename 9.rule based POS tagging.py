#9.Implement a rule-based part-of-speech tagging system using regular expressions using python.
import re

# Define POS tagging rules using regular expressions
pos_rules = [
    (r'\b(?:is|was|were|am|are)\b', 'VB'),   # Verbs like 'is', 'was', 'were'
    (r'\b(?:I|you|he|she|it|we|they)\b', 'PRP'),  # Personal pronouns
    (r'\b(?:the|a|an)\b', 'DT'),  # Determiners
    (r'\b(?:cat|dog|bird)\b', 'NN'),  # Nouns (example: cat, dog, bird)
    (r'\b(?:jumped|ran|walked)\b', 'VBD'),  # Past tense verbs
    (r'\b(?:quick|brown|lazy)\b', 'JJ'),  # Adjectives (example: quick, brown, lazy)
    (r'\b(?:over|under|on)\b', 'IN'),  # Prepositions (example: over, under, on)
]

def rule_based_pos_tag(sentence):
    tagged_sentence = []

    # Tokenize the sentence into words
    words = sentence.split()

    for word in words:
        # Initialize the POS tag as 'NN' (Noun) by default
        pos_tag = 'NN'

        # Apply rules to assign POS tags
        for pattern, tag in pos_rules:
            if re.search(pattern, word, re.IGNORECASE):
                pos_tag = tag
                break

        tagged_sentence.append((word, pos_tag))

    return tagged_sentence

if __name__ == "__main__":
    user_input = input("Enter a sentence for rule-based POS tagging: ")
    tagged_sentence = rule_based_pos_tag(user_input)

    print("Rule-Based POS Tagging:")
    for word, pos_tag in tagged_sentence:
        print(f"Word: {word}, POS Tag: {pos_tag}")
