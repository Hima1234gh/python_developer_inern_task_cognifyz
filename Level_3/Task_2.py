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

class DataVisualizer:
    def __init__(self, uploaded_file):
        self.uploaded_file = uploaded_file
        self.df = None

    def read_file(self):
        if self.uploaded_file.name.endswith(".csv"):
            self.df = pd.read_csv(self.uploaded_file)
        elif self.uploaded_file.name.endswith(".xlsx"):
            self.df = pd.read_excel(self.uploaded_file, engine="openpyxl")

    def file_description(self):
        st.header("📊 Dataset Statistics")
        st.write(self.df.describe())

    def visualize(self):
        st.header("📈 Data Visualization")

        numeric_cols = self.df.select_dtypes(include=np.number).columns.tolist()

        if not numeric_cols:
            st.warning("No numeric columns available for visualization.")
            return

        column = st.selectbox("Select a column", numeric_cols)
        plot_type = st.selectbox(
            "Select plot type",
            ["Histogram", "Box Plot", "Line Plot"]
        )

        fig, ax = plt.subplots()

        if plot_type == "Histogram":
            sns.histplot(self.df[column], kde=True, ax=ax)
        elif plot_type == "Box Plot":
            sns.boxplot(y=self.df[column], ax=ax)
        elif plot_type == "Line Plot":
            ax.plot(self.df[column])

        ax.set_title(f"{plot_type} of {column}")
        st.pyplot(fig)


def main():
    st.title("📊 Interactive Data Visualizer Tool")

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel file",
        type=["csv", "xlsx"]
    )

    if uploaded_file:
        dv = DataVisualizer(uploaded_file)
        dv.read_file()

        st.success("File uploaded successfully!")
        st.dataframe(dv.df.head())

        dv.file_description()
        dv.visualize()
    else:
        st.info("Please upload a dataset to begin.")


if __name__ == "__main__":
    main()
