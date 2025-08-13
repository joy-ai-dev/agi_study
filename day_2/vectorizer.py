from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
doc1 = "I love king"
doc2 = "I love king"
doc3 = "I enjoy playing football"

# Put documents in a list
documents = [doc1, doc2, doc3]

# Step 1: Convert text to TF-IDF vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Step 2: Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix)

print("Cosine similarity matrix:")
print(cosine_sim)
