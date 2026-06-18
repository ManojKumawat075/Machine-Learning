'''import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and sidebar
st.title("TCS Stock Data Dashboard")
st.sidebar.header("Dashboard Controls")

# Data upload
uploaded_file = st.sidebar.file_uploader("Upload your cleaned CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["Date"])
    st.write("### Data Preview", df.head())

    # Simple line chart for Closing Price
    st.write("### Closing Price Over Time")
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Close"])
    ax.set_xlabel("Date")
    ax.set_ylabel("Close")
    st.pyplot(fig)

    # Histogram
    st.write("### Closing Price Distribution")
    # Histogram using matplotlib
    st.write("### Closing Price Distribution")
    fig_hist, ax_hist = plt.subplots()
    ax_hist.hist(df["Close"], bins=30)
    ax_hist.set_xlabel("Close Price")
    ax_hist.set_ylabel("Frequency")
    st.pyplot(fig_hist)


    # Correlation Heatmap with seaborn
    try:
        import seaborn as sns
        import numpy as np
        st.write("### Feature Correlations")
        fig2, ax2 = plt.subplots()
        corr = df.select_dtypes(include=[np.number]).corr()
        sns.heatmap(corr, annot=True, ax=ax2)
        st.pyplot(fig2)
    except ImportError:
        st.warning("Tip: Run 'pip install seaborn' for heatmaps.")
else:
    st.info("Upload your 'tcs_stock_cleaned.csv' to begin.") '''

# Input expression from user
expression = input("Enter an arithmetic expression (+,-,*,/): ")

try:
# Evaluate the arithmetic expression
    result = eval(expression)
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
except Exception as e:
    print("Invalid expression! Please enter a valid arithmetic expression.")

