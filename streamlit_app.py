import streamlit as st
import requests
import json

st.title("Credit Card Fraud Detection Web App")
st.image("image.png")

BACKEND_URL = "https://credit-card-fraud-detection-4mjn.onrender.com/predict/"

st.sidebar.header('Input Features of The Transaction')

sender_name = st.sidebar.text_input("Input Sender ID")
receiver_name = st.sidebar.text_input("Input Receiver ID")
step = st.sidebar.slider("Hours Passed:", 0, 744)
types = st.sidebar.selectbox("Transaction Type", (0,1,2,3,4))
amount = st.sidebar.number_input("Amount", min_value=0, max_value=110000)
oldbalanceorg = st.sidebar.number_input("Sender Balance Before", min_value=0, max_value=110000)
newbalanceorg = st.sidebar.number_input("Sender Balance After", min_value=0, max_value=110000)
oldbalancedest = st.sidebar.number_input("Receiver Balance Before", min_value=0, max_value=110000)
newbalancedest = st.sidebar.number_input("Receiver Balance After", min_value=0, max_value=110000)
isflaggedfraud = st.sidebar.selectbox("System Flag Fraud", (0,1))

if st.button("Detection Result"):
    values = {
        "step": step,
        "types": types,
        "amount": amount,
        "oldbalanceorig": oldbalanceorg,
        "newbalanceorig": newbalanceorg,
        "oldbalancedest": oldbalancedest,
        "newbalancedest": newbalancedest,
        "isflaggedfraud": isflaggedfraud
    }

    try:
        response = requests.post(BACKEND_URL, json=values)
        result = response.json().get("prediction")

        if result == 1:
            st.error("🚨 FRAUDULENT TRANSACTION DETECTED")
        else:
            st.success("✅ LEGITIMATE TRANSACTION")
    except Exception as e:
        st.error("❌ Cannot connect to backend")
        st.write(str(e))
