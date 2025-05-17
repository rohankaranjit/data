import streamlit as st
import pandas as pd

df = pd.read_csv("sales_data.csv")

st.title("Simple Sales Dashboard")

st.subheader("Raw Sales Data")
st.dataframe(df)

region = st.selectbox("Select a Region",df["region"].unique())
filtered_df = df[df["region"]==region]

product = st.selectbox("Select a product", filtered_df["product"].unique())
filtered_df = filtered_df[filtered_df["product"] == product]

st.subheader("Filtered Sales")
st.dataframe(filtered_df)

st.subheader("Sales Over Time")
st.line_chart(filtered_df.set_index("date")["sales"])

