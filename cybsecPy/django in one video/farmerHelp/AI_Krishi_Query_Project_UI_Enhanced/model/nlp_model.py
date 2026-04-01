import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("dataset/agriculture_qa.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["question"])

def get_answer(user_question):
    user_vec = vectorizer.transform([user_question])
    similarity = cosine_similarity(user_vec, X)
    idx = similarity.argmax()
    return data["answer"][idx]
