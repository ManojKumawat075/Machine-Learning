# Mental Health Mood Predictor

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square)

---

## 📌 Project Overview

**Mental Health Mood Predictor** is a machine learning project that analyzes short text input from a user and predicts their current emotional state. Based on the detected mood, the app shows a simple, personalized self-care suggestion.

This is a proof-of-concept: the goal is to demonstrate a full working pipeline (data → model → evaluation → deployment), not to serve as a clinical or diagnostic tool.

---

## 🎯 Objective

- Accept free-text input from the user describing how they feel
- Predict the user's mood using a TF-IDF + Naive Bayes classifier
- Classify the mood into one of four categories — Happy, Sad, Neutral, or Stressed
- Display a personalized suggestion based on the detected mood
- Serve the model through a simple Flask web interface

---

## 📂 Project Structure

```
Mental Health Mood Predictor/
│
├── app.py                                # Flask web application
├── train_model.py                        # Trains and evaluates the model, saves pickles
├── Mood_Predictor_Training.ipynb         # Notebook version — same pipeline, runnable on Colab
├── mood_dataset.csv                      # Labeled dataset (100 examples, 4 classes)
├── model.pkl                             # Trained Naive Bayes model
├── vectorizer.pkl                        # Fitted TF-IDF vectorizer
├── templates/
│   └── index.html                        # Input form + result display
├── Static/
│   └── style.css
└── Mental-Health-Mood-Predictor-README.md
```

---

## 📊 Dataset Details

| Feature | Details |
|---|---|
| Input Feature | Short first-person text describing a feeling |
| Target Labels | Happy, Sad, Neutral, Stressed |
| Size | 100 examples, 25 per class |
| Source | Self-authored for this project (not an external dataset) |
| Format | CSV (`text`, `mood`) |

---

## 🔧 Tech Stack

| Tool / Library | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading and manipulation |
| Scikit-learn | TF-IDF vectorization, Naive Bayes model, train/test split, evaluation |
| Flask | Web application framework |
| HTML & CSS | Frontend user interface |
| Jupyter / Colab | Training notebook |

---

## 🚀 What Was Done

### 1. Dataset
- Wrote a labeled dataset of 100 short sentences across four mood categories (25 each)

### 2. Preprocessing
- Cleaned text via TF-IDF's built-in tokenization (lowercasing, stopword handling using defaults)

### 3. Model Training & Evaluation
- Split data 80/20 with stratification so all four classes are represented in both sets
- Trained a Multinomial Naive Bayes classifier on TF-IDF features
- Evaluated with accuracy and a full classification report (precision/recall/F1 per class)

### 4. Model Saving
- Saved the trained model as `model.pkl` and the vectorizer as `vectorizer.pkl`

### 5. Flask Web Application
- Single-page app: user types how they're feeling, app predicts mood, and shows a suggestion

---

## 📈 Results

**Test accuracy: 40%** on a held-out 20-example test set (5 per class), versus a 25% random baseline for four balanced classes.

| Class | Precision | Recall |
|---|---|---|
| Happy | 0.00 | 0.00 |
| Neutral | 0.33 | 0.60 |
| Sad | 0.67 | 0.40 |
| Stressed | 0.43 | 0.60 |

**Honest takeaway:** 25 examples per class is not enough for TF-IDF + Naive Bayes to learn robust boundaries, especially between emotionally adjacent classes like Sad and Stressed. The model beats random guessing but isn't reliable enough for production use yet.

---

## 🔭 Next Steps

- Expand the dataset to hundreds of examples per class, ideally sourced from a real public emotion-labeled corpus
- Investigate Sad vs. Stressed misclassification specifically
- Compare Naive Bayes against Logistic Regression or a small fine-tuned transformer
- Add a confidence threshold so low-confidence predictions return "not sure" instead of forcing one of four labels
- Add a clear disclaimer and crisis-resource links before any real-world use — this is a self-awareness prompt, not a mental health service

---

## ▶️ How to Run This Project

1. Clone or download this repository
2. Install required libraries:
```bash
pip install pandas scikit-learn flask
```
3. (Optional) Retrain the model:
```bash
python train_model.py
```
4. Run the Flask app:
```bash
python app.py
```
5. Open your browser and go to:
```
http://127.0.0.1:5000
```

> To retrain on Colab instead, upload `Mood_Predictor_Training.ipynb` and `mood_dataset.csv` and run all cells.

---

## 🙋 About Me

**Manoj Kumawat**
B.Tech Computer Science Engineering — PIET, Jaipur (2027)
Aspiring Data Analyst | Machine Learning Enthusiast | Salesforce Developer

📧 manojkumawat37505@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/manoj-kumawat-a18a79290/)
🐙 [GitHub](https://github.com/ManojKumawat075)

---

*If you found this project useful, feel free to ⭐ star the repository!*
