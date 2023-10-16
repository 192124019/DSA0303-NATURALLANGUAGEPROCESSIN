#4Implement a finite-state machine for morphological parsing. In this example,create a simple machine to generate plural forms of English nouns using py
def pluralize_noun(noun):
    # Define a list of pluralization rules
    rules = [
        (r'^(.*[aeiou])y$', r'\1ys'),  # Words ending in 'y' preceded by a vowel
        (r'^(.*[aeiou])y$', r'\1ies'), # Words ending in 'y' preceded by a consonant
        (r'^(.*[sxzh])$', r'\1es'),   # Words ending in 's', 'x', 'z', or 'h'
        (r'^(.*[^aeiou])y$', r'\1ies'), # Words ending in 'y' preceded by a consonant
        (r'^(.*)$', r'\1s')           # Default rule
    ]

    # Apply rules to pluralize the noun
    for pattern, replacement in rules:
        if noun:
            if re.match(pattern, noun):
                return re.sub(pattern, replacement, noun)
    
    return noun

import re

if __name__ == "__main__":
    user_input = input("Enter a singular noun for pluralization: ")
    plural_form = pluralize_noun(user_input)
    print(f"Plural form: {plural_form}")

