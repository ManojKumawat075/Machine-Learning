# TCS Stock Price Forecasting — Time Series Analysis

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=keras&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

## 📌 Project Overview

This project analyzes **historical stock market data of Tata Consultancy Services (TCS)** and forecasts future stock prices using both statistical and deep learning models. The project compares the performance of **ARIMA**, **SARIMA**, and **LSTM** models to identify which approach best captures the patterns in TCS stock price movement.

---

## 🎯 Objective

- Analyze historical TCS stock price trends over 248+ trading days
- Perform exploratory data analysis to understand price behavior
- Build and compare forecasting models — ARIMA, SARIMA, and LSTM
- Identify which model performs best for stock price prediction
- Help investors and analysts make more data-driven decisions

---

## 📂 Project Structure

```
TCS-Stock-Forecasting/
│
├── notebook.ipynb        # Main analysis and forecasting notebook
├── tcs_stock.csv         # Historical TCS stock data
└── README.md             # Project documentation
```

---

## 📊 Dataset Details

| Feature | Details |
|---|---|
| Stock | Tata Consultancy Services (TCS) |
| Records | 248+ trading days |
| Format | CSV |
| Key Columns | Date, Open, High, Low, Close, Volume, VWAP, Trades, Deliverable Volume |

---

## 🔧 Tech Stack

| Tool / Library | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading, cleaning, and manipulation |
| NumPy | Numerical computation |
| Matplotlib | Charts and trend visualization |
| Seaborn | Statistical plots and distribution analysis |
| Scikit-learn | Data preprocessing and scaling |
| Statsmodels | ARIMA and SARIMA model building |
| TensorFlow / Keras | LSTM deep learning model |
| Jupyter Notebook | Development environment |

---

## 🚀 What Was Done

### 1. Data Loading & Inspection
- Loaded TCS historical stock data from CSV
- Checked shape, data types, null values, and basic statistics

### 2. Data Cleaning & Preprocessing
- Handled missing values and formatted the date column
- Scaled numerical features using MinMaxScaler for LSTM input
- Prepared train and test splits for model evaluation

### 3. Exploratory Data Analysis (EDA)
- Plotted closing price trends over time
- Analyzed daily returns and price volatility
- Studied correlation between Open, High, Low, Close, and Volume
- Visualized distribution of stock features using histograms and box plots

### 4. Feature Engineering
- Extracted time-based features from the date column
- Created lag features and rolling averages for trend analysis

### 5. Model Building & Forecasting

#### 📉 ARIMA (AutoRegressive Integrated Moving Average)
- Applied stationarity tests (ADF Test)
- Selected optimal p, d, q parameters
- Generated forecast and plotted against actual prices

#### 📉 SARIMA (Seasonal ARIMA)
- Extended ARIMA to handle seasonal patterns
- Selected seasonal parameters and generated seasonal forecast

#### 🤖 LSTM (Long Short-Term Memory — Deep Learning)
- Built a sequential LSTM model using TensorFlow/Keras
- Trained on 80% of data and tested on remaining 20%
- Plotted predicted vs actual closing prices

### 6. Model Comparison
- Compared all three models on forecast accuracy
- Identified best performing model for TCS stock prediction

---

## 📈 Key Findings

- TCS stock showed clear **upward and downward trends** over the analyzed period
- **LSTM outperformed** ARIMA and SARIMA in capturing non-linear price patterns
- **ARIMA and SARIMA** performed well for short-term linear trend forecasting
- Daily return analysis revealed **high volatility on specific trading days**
- Strong **positive correlation** was found between Open, High, Low, and Close prices

---

## ▶️ How to Run This Project

1. Clone or download this repository
2. Install required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels tensorflow jupyter
```
3. Open the notebook:
```bash
jupyter notebook notebook.ipynb
```
4. Run all cells from top to bottom

---

## 📉 Models Used — Quick Reference

| Model | Type | Best For |
|---|---|---|
| ARIMA | Statistical | Short-term linear forecasting |
| SARIMA | Statistical | Forecasting with seasonal patterns |
| LSTM | Deep Learning | Long-term non-linear pattern forecasting |

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
