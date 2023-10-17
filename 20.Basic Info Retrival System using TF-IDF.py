#20.Implement a basic information retrieval system using TF-IDF (Term Frequency-Inverse Document Frequency) for document ranking using python.
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

nltk.download('stopwords')

# Sample documents (you can replace these with your own documents)
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

# Sample query
query = "This is the second document."

# Step 1: Preprocess the documents and query
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    words = nltk.word_tokenize(text.lower())
    words = [word for word in words if word.isalnum()]
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

processed_documents = [preprocess_text(doc) for doc in documents]
processed_query = preprocess_text(query)

# Step 2: Calculate TF-IDF scores
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(processed_documents)

# Step 3: Calculate the cosine similarity between the query and documents
query_vector = tfidf_vectorizer.transform([processed_query])
cosine_similarities = linear_kernel(query_vector, tfidf_matrix).flatten()

# Step 4: Rank the documents based on cosine similarity
document_scores = list(enumerate(cosine_similarities))
document_scores = sorted(document_scores, key=lambda x: x[1], reverse=True)

# Display the ranked documents
for index, score in document_scores:
    print(f"Document {index + 1} - Similarity Score: {score:.2f}")
