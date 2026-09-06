import streamlit as st
import pickle

st.set_page_config(page_title="Mental Health Mood Predictor", page_icon="💜")

@st.cache_resource
def load_model():
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    return model, vectorizer

model, vectorizer = load_model()

SUGGESTIONS = {
    "Happy": "Keep doing what makes you happy 😊",
    "Sad": "Talk to someone you trust 💬",
    "Stressed": "Take a short break and relax 🧘",
    "Neutral": "Stay balanced and positive 🌿",
}

st.title("💜 Mental Health Mood Predictor")
st.write("Share your feelings and let the model estimate your mood.")

text = st.text_area("How are you feeling today?", placeholder="Type your feelings here...")

if st.button("✨ Predict My Mood"):
    if text.strip():
        vec = vectorizer.transform([text])
        prediction = model.predict(vec)[0]
        st.subheader(f"📊 Your Mood: {prediction}")
        st.write(SUGGESTIONS.get(prediction, "Take care of yourself today."))
    else:
        st.warning("Please type something first.")

st.caption("Note: this is a small proof-of-concept model (100 training examples, ~40% test accuracy) — not a diagnostic tool.")
