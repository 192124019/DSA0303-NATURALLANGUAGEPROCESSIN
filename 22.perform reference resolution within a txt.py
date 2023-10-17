#22. Create a python program that performs reference resolution within a text.
import re

def resolve_pronouns(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)

    resolved_text = []

    for sentence in sentences:
        tokens = sentence.split()
        antecedent = None

        for token in tokens:
            if token.lower() in ("he", "she", "it", "they"):
                if antecedent:
                    resolved_text.append(antecedent)
                    antecedent = None
                resolved_text.append(token)
            else:
                if antecedent:
                    resolved_text.append(antecedent)
                antecedent = token
                resolved_text.append(token)

    return " ".join(resolved_text)

# Get user input
text = input("Enter a text with pronouns to resolve: ")

# Perform pronoun resolution
resolved_text = resolve_pronouns(text)
print("Resolved Text:")
print(resolved_text)
