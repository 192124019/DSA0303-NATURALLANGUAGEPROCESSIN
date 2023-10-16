#6.Implement a basic N-gram model for text generation. For example, generate text using a bigram model using python.
import random

def build_bigram_model(text):
    words = text.split()
    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
    bigram_model = {}
    for w1, w2 in bigrams:
        if w1 in bigram_model:
            bigram_model[w1].append(w2)
        else:
            bigram_model[w1] = [w2]
    return bigram_model

def generate_text(bigram_model, start_word, num_words=20):
    generated_text = [start_word]
    current_word = start_word

    for _ in range(num_words - 1):
        if current_word in bigram_model:
            next_word = random.choice(bigram_model[current_word])
            generated_text.append(next_word)
            current_word = next_word
        else:
            break

    return " ".join(generated_text)

if __name__ == "__main__":
    user_input = input("Enter a text: ")
    bigram_model = build_bigram_model(user_input)

    start_word = input("Enter a starting word: ")
    num_words = int(input("Enter the number of words to generate: "))

    generated_text = generate_text(bigram_model, start_word, num_words)
    print("Generated Text:")
    print(generated_text)
#output
#Enter a text: The quick brown fox jumps over the lazy dog
#Enter a starting word: quick
#Enter the number of words to generate: 10
#Generated Text:
#quick brown fox jumps over the lazy dog
