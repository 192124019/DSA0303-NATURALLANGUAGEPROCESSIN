#8.Implement a simple stochastic part-of-speech tagging algorithm using a basic probabilisticmodel to assign POS tags using python.
import random

def stochastic_pos_tag(sentence):
    words = sentence.split()
    pos_tags = []

    for word in words:
        # Assign a POS tag probabilistically (simplified model)
        pos_tag = random.choice(['N', 'V'])
        pos_tags.append(pos_tag)

    return list(zip(words, pos_tags))

if __name__ == "__main__":
    user_input = input("Enter a sentence for probabilistic POS tagging: ")
    tagged_words = stochastic_pos_tag(user_input)

    print("Probabilistic POS Tagging:")
    for word, pos_tag in tagged_words:
        print(f"Word: {word}, POS Tag: {pos_tag}")
