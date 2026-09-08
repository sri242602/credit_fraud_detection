import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Health Insurance Fraud Detection",
    page_icon="🏥",
    layout="wide"
)

# -----------------------------
# Load Trained Model
# -----------------------------
model = joblib.load("insurance_fraud_model.pkl")

st.title("🏥 Health Insurance Fraud Detection")
st.write("Enter the insurance claim details below.")

# =====================================================
# Replace these with your actual dataset column names
# (Do NOT include the target column Is_Fraudulent)
# =====================================================

features = [
    "Age",
    "Gender",
    "Policy_Type",
    "Premium_Amount",
    "Claim_Amount",
    "Hospital_Days",
    "Diagnosis_Code",
    "Hospital_Type",
    "Previous_Claims",
    "Chronic_Disease"
]

data = {}

st.subheader("Enter Claim Details")

for feature in features:
    data[feature] = st.number_input(feature, value=0)

input_df = pd.DataFrame([data])

if st.button("Predict"):

    prediction = model.predict(input_df)[0]

    st.markdown("---")

    if prediction == 1:
        st.error("⚠ Fraudulent Insurance Claim")S
    else:
        st.success("✅ Genuine Insurance Claim")

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_df)[0][1]
        st.write(f"Fraud Probability: **{probability:.2%}**")