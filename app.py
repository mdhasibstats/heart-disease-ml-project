import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model pipeline
pipeline = joblib.load("model/svc_final_pipeline.pkl")

# Page configuration
st.set_page_config(page_title="Heart Disease Prediction App", page_icon="❤️", layout="centered")

st.title("❤️ Heart Disease Prediction App")
st.markdown("Enter your health data below to check your risk of heart disease.")

# user inputs
age = st.number_input("Age", min_value=1, max_value=120, value=45)

sex = st.selectbox("Sex", ["Male", "Female"])
sex = 1 if sex == "Male" else 0

cp = st.selectbox("Chest Pain Type (cp)", [
    "Typical Angina (0)",
    "Atypical Angina (1)",
    "Non-anginal Pain (2)",
    "Asymptomatic (3)"
])
cp = int(cp.split("(")[-1][0]) 

trestbps = st.number_input("Resting Blood Pressure(trestbps)", min_value=80, max_value=200, value=120)

chol = st.number_input("Serum Cholesterol (mg/dl)(chol)", min_value=100, max_value=600, value=200)

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", ["Yes", "No"])
fbs = 1 if fbs == "Yes" else 0

restecg = st.selectbox("Resting ECG (restecg)", [
    "Normal (0)",
    "Having ST-T wave abnormality (1)",
    "Probable/Definite Left Ventricular Hypertrophy (2)"
])
restecg = int(restecg.split("(")[-1][0])

thalach = st.number_input("Maximum Heart Rate Achieved(thalach)", min_value=60, max_value=220, value=150)

exang = st.selectbox("Exercise Induced Angina (exang)", ["Yes", "No"])
exang = 1 if exang == "Yes" else 0

oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=6.0, step=0.1, value=1.0)

slope = st.selectbox("Slope of Peak Exercise ST Segment (slope)", [
    "Upsloping (0)",
    "Flat (1)",
    "Downsloping (2)"
])
slope = int(slope.split("(")[-1][0])

ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (ca)", [0, 1, 2, 3, 4])

thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])

# Prediction Button
if st.button("🔍 Predict"):
    columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
           'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

    input_df = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg,
                          thalach, exang, oldpeak, slope, ca, thal]], columns=columns)

    prediction = pipeline.predict(input_df)[0]
    prob = pipeline.predict_proba(input_df)[0][1]

    
    # Show result
    if prediction == 1:
        st.error(f"⚠️ High Risk: The patient is likely to have heart disease.\nProbability: {prob:.2%}")
    else:
        st.success(f"✅ Low Risk: The patient is unlikely to have heart disease.\nProbability: {prob:.2%}")