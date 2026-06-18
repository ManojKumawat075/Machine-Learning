# Mental Health Mood Predictor

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

## 📌 Project Overview

**Mental Health Mood Predictor** is a machine learning project that analyzes text input from a user and predicts their current emotional state. Based on the detected mood, the system provides simple and personalized suggestions to support their mental well-being.

Many people feel stressed, sad, or emotionally low but may not always recognize their emotional state or have immediate access to mental health support. This project aims to bridge that gap through a simple, accessible, and easy-to-use web interface.

---

## 🎯 Objective

- Accept free-text input from the user describing how they feel
- Predict the user's mood from the text using a machine learning model
- Classify the mood into one of four categories — Happy, Sad, Neutral, or Stressed
- Display personalized suggestions based on the detected mood
- Provide an interactive and clean web interface using Flask

---

## 📂 Project Structure

```
Mental-Health-Mood-Predictor/
│
├── app.py                  # Flask web application
├── model/
│   ├── mood_model.pkl      # Trained Naive Bayes model
│   └── tfidf_vectorizer.pkl  # Saved TF-IDF vectorizer
├── templates/
│   ├── index.html          # Home page — text input form
│   └── result.html         # Result page — mood and suggestions
├── notebook.ipynb          # Model training and evaluation notebook
├── dataset.csv             # Text-based emotion dataset
└── README.md               # Project documentation
```

---

## 📊 Dataset Details

| Feature | Details |
|---|---|
| Input Feature | User text / sentences |
| Target Labels | Happy, Sad, Neutral, Stressed |
| Source | Kaggle Emotion Dataset / Custom dataset |
| Format | CSV |

---

## 🔧 Tech Stack

| Tool / Library | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading and manipulation |
| NumPy | Numerical operations |
| Scikit-learn | TF-IDF vectorization and Naive Bayes model |
| Flask | Web application framework |
| HTML & CSS | Frontend user interface |
| Jupyter Notebook | Model training and experimentation |

---

## 🚀 What Was Done

### 1. Data Loading & Inspection
- Loaded the emotion text dataset
- Checked class distribution across all four mood labels
- Verified data quality and handled missing values

### 2. Data Preprocessing
- Cleaned text — removed punctuation, special characters, and extra spaces
- Converted all text to lowercase
- Applied **TF-IDF Vectorization** to convert text into numerical features

### 3. Model Building
- Split data into training and testing sets (80/20)
- Trained a **Multinomial Naive Bayes** classifier on TF-IDF features
- Evaluated model using accuracy score and classification report

### 4. Model Saving
- Saved the trained model as `mood_model.pkl` using joblib
- Saved the TF-IDF vectorizer as `tfidf_vectorizer.pkl` for reuse in Flask

### 5. Flask Web Application
- Built a simple web app with two pages — input form and result page
- User types how they are feeling in a text box
- App loads the saved model, vectorizes the input, and predicts the mood
- Result page shows the predicted mood and personalized suggestions

### 6. Mood-based Suggestions
| Mood | Suggestion Shown |
|---|---|
| 😊 Happy | Keep up the positive energy! Share your happiness with someone today. |
| 😢 Sad | It's okay to feel sad. Try talking to someone you trust or take a short walk. |
| 😐 Neutral | You seem calm. A good time to focus on your goals or learn something new. |
| 😰 Stressed | Take a deep breath. Try a short break, some water, and step away from screens. |

---

## 📈 Key Findings

- **Naive Bayes with TF-IDF** performed well for short emotional text classification
- The model was able to distinguish between **Stressed and Sad** effectively, which are often confused
- **TF-IDF** captured important emotional keywords across all four mood categories
- The web interface made the model accessible without any technical knowledge

---

## ▶️ How to Run This Project

1. Clone or download this repository
2. Install required libraries:
```bash
pip install pandas numpy scikit-learn flask jupyter
```
3. Run the Flask app:
```bash
python app.py
```
4. Open your browser and go to:
```
http://127.0.0.1:5000
```
5. Type how you are feeling and get your mood prediction!

> **Note:** To retrain the model, open `notebook.ipynb` in Jupyter and run all cells.

---

## 🖥️ How It Works

```
User types text
      ↓
Text is cleaned and vectorized using TF-IDF
      ↓
Naive Bayes model predicts the mood
      ↓
Result page shows mood + personalized suggestion
```

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
