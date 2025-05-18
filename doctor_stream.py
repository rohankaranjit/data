import streamlit as st
import pandas as pd

df = pd.read_csv("doctor.csv")

df["remarks"]=df["remarks"].fillna("No remarks ")
df["available_today"] = df["available_today"].fillna("No")

availability = st.selectbox("Do you want to see available doctors",["Yes","No"])

filtered_df = df[df["available_today"].str.lower() == availability.lower()]

st.subheader("These are available doctors")

if not filtered_df.empty:
    st.dataframe(filtered_df[["doctor_id","name","specialization" , "start_time","end_time"]])
else:
    st.warning(f"No doctors are {"available" if availability == "Yes" else "booked"} today.")