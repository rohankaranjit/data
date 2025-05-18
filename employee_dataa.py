import pandas as pd
import streamlit as st
import altair as alt

st.title("Employees Data Dashboard")

df = pd.read_csv("employee_data.csv")

st.dataframe(df)

missing_value = df.isnull().sum()
st.write("These are missing null per column")
st.write(missing_value)

df["name"] = df["name"].fillna("Unknown")

df["department"] = df["department"].fillna("Not Assigned")

median_salary = df["salary"].mean()
df["salary"] = df["salary"].fillna(median_salary)

avg_performance = df["performance_score"].mean()
df["performance_score"] = df["performance_score"].fillna(avg_performance)

df["bonus"] = df["bonus"].fillna(0)

df["joining_date"] = df["joining_date"].fillna("Unknown")
df["employee_id"] = df["employee_id"].fillna(109)

df["notes"] = df["notes"].fillna("Fucked UP") 

st.write("Cleaned Data")
st.dataframe(df)

#SUMMARY

st.write("Average Salary",round(df["salary"].mean(),2))
st.write("Average Performance",round(df["performance_score"].mean(),2))
st.write("Total Bonus given",round(df["bonus"].sum(),2))

#Filter by department

departments = df["department"].unique()
selected_dept = st.selectbox("Select Depatment",departments)
filtered_data = df[df["department"] == selected_dept]

st.subheader(f"Employees in {selected_dept}")
st.dataframe(filtered_data)

st.subheader("Performance Vs Salary")

scatter = alt.Chart(filtered_data).mark_circle(size=100).encode(
    x='performance_score',
    y='salary',
    tooltip=['name', 'department', 'performance_score', 'salary']
).interactive()

st.altair_chart(scatter, use_container_width=True)