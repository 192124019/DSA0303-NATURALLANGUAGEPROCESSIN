#10.Implement transformation-based tagging using a set of transformation rules, apply a simple rule to tag words using python.
def transform_based_pos_tag(sentence):
    tagged_sentence = []

    # Tokenize the sentence into words
    words = sentence.split()

    for word in words:
        # Apply the transformation rule
        if word.lower().endswith("ing"):
            pos_tag = "V"  # Verb
        else:
            pos_tag = "N"  # Noun

        tagged_sentence.append((word, pos_tag))

    return tagged_sentence

if __name__ == "__main__":
    user_input = input("Enter a sentence for transformation-based POS tagging: ")
    tagged_sentence = transform_based_pos_tag(user_input)

    print("Transformation-Based POS Tagging:")
    for word, pos_tag in tagged_sentence:
        print(f"Word: {word}, POS Tag: {pos_tag}")
