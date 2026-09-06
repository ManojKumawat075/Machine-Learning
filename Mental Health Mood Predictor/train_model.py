import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dataset (you can expand later)
data = {
    "text": [
        "I am very happy",
        "I feel sad and lonely",
        "I am stressed about exams",
        "I feel normal today",
        "I am excited",
        "I feel depressed",
        "I am tired and anxious",
        "Life is beautiful",
        "I feel very low",
        "I am calm and relaxed"
    ],
    "mood": [
        "Happy", "Sad", "Stressed", "Neutral", "Happy",
        "Sad", "Stressed", "Happy", "Sad", "Neutral"
    ]
}

df = pd.DataFrame(data)

# Convert text to numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["mood"]

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained and saved!")