#23.Develop a python program that evaluates the coherence of a given text.
from gensim.models import CoherenceModel
from gensim.corpora import Dictionary
from gensim.models.ldamodel import LdaModel

def evaluate_coherence(texts):
    # Create a dictionary and a corpus
    dictionary = Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    # Build an LDA model
    lda_model = LdaModel(corpus, num_topics=5, id2word=dictionary)

    # Calculate coherence score
    coherence_model = CoherenceModel(model=lda_model, texts=texts, dictionary=dictionary, coherence='c_v')
    coherence_score = coherence_model.get_coherence()

    return coherence_score

# Example usage
text1 = ["This is the first sentence of the text.", "It talks about coherence evaluation."]
text2 = ["The quick brown fox jumps over the lazy dog.", "This is a completely unrelated sentence."]
texts = [text1, text2]

coherence_score = evaluate_coherence(texts)
print(f"Coherence Score: {coherence_score}")
