import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("salary_model.pkl")

# App title
st.title("💼 Salary Prediction App")

st.write("Predict salary based on Age, Experience, Education, Gender, and Job Title")

# User Inputs
age = st.number_input("Age", min_value=18, max_value=65, value=25)
experience = st.number_input("Years of Experience", min_value=0, max_value=40, value=2)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

education = st.selectbox(
    "Education Level",
    ["High School", "Bachelor", "Master", "PhD"]
)

job_title = st.text_input(
    "Job Title",
    value="Software Engineer"
)

# Predict button
if st.button("Predict Salary"):
    
    input_data = pd.DataFrame({
        "Age": [age],
        "Years of Experience": [experience],
        "Gender": [gender],
        "Education Level": [education],
        "Job Title": [job_title]
    })

    prediction = model.predict(input_data)

    st.success(f"💰 Predicted Salary: {prediction[0]:.2f}")
