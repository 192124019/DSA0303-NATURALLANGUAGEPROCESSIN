#7.Write program using the NLTK library to perform part-of-speech tagging on a text
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tag_text(text):
    tokens = nltk.word_tokenize(text)
    tagged_words = nltk.pos_tag(tokens)
    return tagged_words

if __name__ == "__main__":
    user_input = input("Enter a sentence for part-of-speech tagging: ")
    tagged_words = pos_tag_text(user_input)

    print("Part-of-Speech Tagging:")
    for word, pos_tag in tagged_words:
        print(f"Word: {word}, POS Tag: {pos_tag}")
