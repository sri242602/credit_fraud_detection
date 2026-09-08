import streamlit as st
import pickle
import numpy as np

# -------------------------
# Load Model and Scaler
# -------------------------
model = pickle.load(open("fraud_detection_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# -------------------------
# Title
# -------------------------
st.title("💳 Credit Card Fraud Detection")
st.write("Predict whether a credit card transaction is Fraudulent or Genuine.")

st.markdown("---")

# -------------------------
# Sidebar
# -------------------------
st.sidebar.header("Enter Transaction Details")

time = st.sidebar.number_input("Time", value=0.0)
amount = st.sidebar.number_input("Amount", value=0.0)

V1 = st.sidebar.number_input("V1", value=0.0)
V2 = st.sidebar.number_input("V2", value=0.0)
V3 = st.sidebar.number_input("V3", value=0.0)
V4 = st.sidebar.number_input("V4", value=0.0)
V5 = st.sidebar.number_input("V5", value=0.0)
V6 = st.sidebar.number_input("V6", value=0.0)
V7 = st.sidebar.number_input("V7", value=0.0)
V8 = st.sidebar.number_input("V8", value=0.0)
V9 = st.sidebar.number_input("V9", value=0.0)
V10 = st.sidebar.number_input("V10", value=0.0)
V11 = st.sidebar.number_input("V11", value=0.0)
V12 = st.sidebar.number_input("V12", value=0.0)
V13 = st.sidebar.number_input("V13", value=0.0)
V14 = st.sidebar.number_input("V14", value=0.0)
V15 = st.sidebar.number_input("V15", value=0.0)
V16 = st.sidebar.number_input("V16", value=0.0)
V17 = st.sidebar.number_input("V17", value=0.0)
V18 = st.sidebar.number_input("V18", value=0.0)
V19 = st.sidebar.number_input("V19", value=0.0)
V20 = st.sidebar.number_input("V20", value=0.0)
V21 = st.sidebar.number_input("V21", value=0.0)
V22 = st.sidebar.number_input("V22", value=0.0)
V23 = st.sidebar.number_input("V23", value=0.0)
V24 = st.sidebar.number_input("V24", value=0.0)
V25 = st.sidebar.number_input("V25", value=0.0)
V26 = st.sidebar.number_input("V26", value=0.0)
V27 = st.sidebar.number_input("V27", value=0.0)
V28 = st.sidebar.number_input("V28", value=0.0)

# -------------------------
# Prediction Button
# -------------------------
if st.button("Predict Transaction"):

    features = np.array([[time,
                          V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,
                          V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,
                          V21,V22,V23,V24,V25,V26,V27,V28,
                          amount]])

    scaled = scaler.transform(features)

    prediction = model.predict(scaled)

    if prediction[0] == 0:
        st.success("✅ Genuine Transaction")
    else:
        st.error("🚨 Fraudulent Transaction")

st.markdown("---")

st.info("Developed using Streamlit and Machine Learning.")