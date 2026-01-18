"""Build a tool that takes a dataset and
generates interactive visualizations using
libraries such as Matplotlib, Seaborn, or
Plotly. This task will enhance their
understanding of data visualization principles
and plotting techniques."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Automated Data Processor", layout="centered")

st.title("📊 Automated File Processing System")

# File upload
uploaded_file = st.file_uploader(
    "Upload your CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file:
    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")

    # Show raw data
    st.subheader("🔍 Preview of Data")
    st.dataframe(df.head())

    # Basic cleaning using NumPy & pandas
    st.subheader("🧹 Data Cleaning")
    df = df.dropna()
    df = df.select_dtypes(include=np.number)

    st.write("After removing missing values:")
    st.dataframe(df.head())

    # Statistics
    st.subheader("📈 Statistical Summary")
    st.write(df.describe())

    # Visualization
    st.subheader("📊 Visualization")

    column = st.selectbox("Select column for visualization", df.columns)

    fig, ax = plt.subplots()
    sns.histplot(df[column], kde=True, ax=ax)
    ax.set_title(f"Distribution of {column}")

    st.pyplot(fig)
