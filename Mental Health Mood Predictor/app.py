from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def get_suggestion(mood):
    if mood == "Happy":
        return "Keep doing what makes you happy 😊"
    elif mood == "Sad":
        return "Talk to someone you trust 💬"
    elif mood == "Stressed":
        return "Take a short break and relax 🧘"
    else:
        return "Stay balanced and positive 🌿"

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    suggestion = None

    if request.method == "POST":
        user_input = request.form["text"]

        vec = vectorizer.transform([user_input])
        pred = model.predict(vec)[0]

        prediction = pred
        suggestion = get_suggestion(pred)

    return render_template("index.html", prediction=prediction, suggestion=suggestion)

if __name__ == "__main__":
    app.run(debug=True)