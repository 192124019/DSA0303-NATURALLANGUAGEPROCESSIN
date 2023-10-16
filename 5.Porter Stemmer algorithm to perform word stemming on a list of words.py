#5.Use the Porter Stemmer algorithm to perform word stemming on a list of words using python libraries get input from user
import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt')

def stem_words(word_list):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in word_list]
    return stemmed_words

if __name__ == "__main__":
    user_input = input("Enter a list of words (separated by spaces): ")
    words = user_input.split()

    stemmed_words = stem_words(words)

    print("Original words:", words)
    print("Stemmed words:", stemmed_words)
