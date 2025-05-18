import streamlit as st
import pandas as pd

st.header("📁CSV Uploader and Reader")

uploaded_file = st.file_uploader("Upload your CSV",type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    st.subheader("Raw Data")

    st.dataframe(df)
    st.write(f"Rows: {df.shape[0]} | Column: {df.shape[1]}")
    st.write("Number of columns in you CSV" , list(df.columns))

    filter_column = st.selectbox("Select a column to filter by",df.columns)
    filter_value = st.selectbox("Select value",df[filter_column].unique())

    filtered_df = df[df[filter_column] == filter_value]
    min_value = float(df[filter_column].min())
    max_value = float(df[filter_column].max())

    selected_range = st.slider("Select range" , min_value , max_value , (min_value,max_value))
    filtered_df = df[df[filter_column].between(*selected_range)]

    st.dataframe(filtered_df) 
   


else:
    st.info("Send you CSV to get started")