import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("TCS Stock Data Dashboard")
st.sidebar.header("Dashboard Controls")

uploaded_file = st.sidebar.file_uploader("Upload tcs_stock_cleaned.csv", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["Date"])
    st.write("### Data Preview", df.head())

    st.write("### Closing Price Over Time")
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Close"])
    ax.set_xlabel("Date")
    ax.set_ylabel("Close")
    st.pyplot(fig)

    st.write("### Closing Price Distribution")
    fig_hist, ax_hist = plt.subplots()
    ax_hist.hist(df["Close"], bins=30)
    ax_hist.set_xlabel("Close Price")
    ax_hist.set_ylabel("Frequency")
    st.pyplot(fig_hist)

    st.write("### Feature Correlations")
    fig2, ax2 = plt.subplots()
    corr = df.select_dtypes(include=[np.number]).corr()
    sns.heatmap(corr, annot=True, ax=ax2)
    st.pyplot(fig2)
else:
    st.info("Upload 'tcs_stock_cleaned.csv' to begin.")
