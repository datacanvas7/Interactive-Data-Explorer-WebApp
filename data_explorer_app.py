# 📊 Interactive CSV Data Explorer
# This web app lets users upload a CSV file, preview the data, filter it by column values,
# and visualize relationships between variables — all through an easy Streamlit interface.
# Inspired by this [YouTube tutorial](https://www.youtube.com/watch?v=2siBrMsqF44&list=PPSV).

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App Title and Description
st.set_page_config(page_title="Interactive Data Explorer", layout="wide")
st.title("📊 Interactive Data Explorer")
st.markdown("""
### This app has been developed by [Yawar Ali](https://github.com/datacanvas7) 
           
This Streamlit app allows you to **upload, explore, filter, and visualize** your own Excel files interactively.

Simply upload a dataset to get started — no coding required!
""")

# File Upload
uploaded_file = st.file_uploader("📂 Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read file based on type
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    st.dataframe(df)

    st.subheader("🔍 Data Preview")
    st.write(df.head())

    st.subheader("📈 Data Summary")
    st.write(df.describe())

    st.subheader("🎯 Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)

    if selected_column:
        unique_values = df[selected_column].unique()
        selected_value = st.selectbox(f"Select value for {selected_column}", unique_values)

        filtered_data = df[df[selected_column] == selected_value]
        st.dataframe(filtered_data)

        st.subheader("📊 Data Visualization")
        x_column = st.selectbox("Select x-axis column", columns, index=0)
        y_column = st.selectbox("Select y-axis column", columns, index=1)

        if st.button("Generate Plot"):
            if x_column in filtered_data.columns and y_column in filtered_data.columns:
                st.line_chart(filtered_data.set_index(x_column)[y_column])
            else:
                st.error("Selected columns are not in filtered data")
        else:
            st.write("Waiting for plot generation...")

else:
    st.info("Please upload a CSV file to start.")

