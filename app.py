import streamlit as st
import pandas as pd
import pickle

# Load your trained model
with open("insurance_premium_model.pkl", "rb") as f:
    model = pickle.load(f)
    
st.title("Insurance Premium Prediction App")

st.header("Enter your details:")

# Input widgets
age = st.number_input("Age", min_value=18, max_value=72, value=30)

gender = st.selectbox("Gender", ["Male", "Female"])

region = st.selectbox("Region", ["Southeast", "Southwest", "Northeast", "Northwest"])  # adjust according to your data

marital_status = st.selectbox("Marital Status", ["Unmarried", "Married"])

num_dependants = st.number_input("Number of Dependants", min_value=0, max_value=5, value=0)

bmi_category = st.selectbox("BMI Category", ["Underweight", "Normal", "Overweight", "Obesity"])  # adjust categories

smoking_status = st.selectbox("Smoking Status", ["No Smoking","Regular","Occasional"])

employment_status = st.selectbox("Employment Status", ["Salaried", "Freelancer", "Self-Employed"])  # adjust categories

income_lakhs = st.number_input("Income in Lakhs", min_value=1.0, max_value=67.0, value=5.0, step=0.1)

medical_history = st.selectbox("Medical History",  ["No Disease", "Diabetes", "High blood pressure", "Thyroid", "Heart disease", "Diabetes & High blood pressure", "High blood pressure & Heart disease", "Diabetes & Thyroid", "Diabetes & Heart disease"])  # adjust categories

insurance_plan = st.selectbox("Insurance Plan", ["Bronze", "Silver", "Gold"])  # adjust categories

# Button to predict
if st.button("Predict Annual Premium Amount"):
    # Prepare input data as a dataframe
    input_df = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Region": [region],
        "Marital_status": [marital_status],
        "Number Of Dependants": [num_dependants],
        "BMI_Category": [bmi_category],
        "Smoking_Status": [smoking_status],
        "Employment_Status": [employment_status],
        "Income_Lakhs": [income_lakhs],
        "Medical History": [medical_history],
        "Insurance_Plan": [insurance_plan]
    })

    # Prediction
    pred = model.predict(input_df)
    st.success(f"Predicted Annual Premium Amount: ₹{round(pred[0], 2)}")
