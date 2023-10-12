import nltk

# Download NLTK data (if not already downloaded)
nltk.download('punkt')

# Sample text
text = "She wanted to go out. However, it was raining."

# Tokenize the text into sentences
sentences = nltk.sent_tokenize(text)

# Identify discourse markers
discourse_markers = ["however", "but", "although", "while"]

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    for word in words:
        if word.lower() in discourse_markers:
            print(f"Discourse marker found: {word} (in sentence: {sentence})")
