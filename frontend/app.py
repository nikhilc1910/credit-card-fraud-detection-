import streamlit as st
import requests
import json

st.set_page_config(page_title="Credit Card Fraud Detection Web App", layout="wide")

st.title("Credit Card Fraud Detection Web App")
st.image("image.png")

st.write("""
## About
This Streamlit app predicts **fraudulent credit card transactions** using a Machine Learning model
hosted on a FastAPI backend deployed on Render.

Enter all transaction details on the left, then click **Detection Result**.
""")

# Your Render FastAPI backend URL
API_URL = "https://credit-card-fraud-detection-4mjn.onrender.com/predict"

# Sidebar inputs
st.sidebar.header("Input Features of The Transaction")

sender_name = st.sidebar.text_input("Sender ID")
receiver_name = st.sidebar.text_input("Receiver ID")
step = st.sidebar.slider("Transaction Hour (0–744)", 0, 744, 0)

st.sidebar.write("""
### Transaction Type:
0 = Cash In  
1 = Cash Out  
2 = Debit  
3 = Payment  
4 = Transfer  
""")

types = st.sidebar.selectbox("Select Transaction Type", (0, 1, 2, 3, 4))

amount = st.sidebar.number_input("Amount ($)", min_value=0, max_value=500000)
oldbalanceorg = st.sidebar.number_input("Sender Balance Before Transaction", min_value=0, max_value=500000)
newbalanceorg = st.sidebar.number_input("Sender Balance After Transaction", min_value=0, max_value=500000)
oldbalancedest = st.sidebar.number_input("Receiver Balance Before Transaction", min_value=0, max_value=500000)
newbalancedest = st.sidebar.number_input("Receiver Balance After Transaction", min_value=0, max_value=500000)

# System flag fraud
isflaggedfraud = 1 if amount >= 200000 else 0

# Prediction button
if st.button("Detection Result"):

    if sender_name == "" or receiver_name == "":
        st.error("Please enter both Sender ID and Receiver ID!")
    else:
        payload = {
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
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                result = response.json().get("prediction")

                final = "Fraudulent ❌" if result == 1 else "Legitimate ✅"

                st.subheader("Prediction Result")
                st.write(f"Transaction between **{sender_name}** and **{receiver_name}** is:")
                st.success(final) if result == 0 else st.error(final)

            else:
                st.error(f"API ERROR: Status Code {response.status_code}")
                st.write(response.text)

        except Exception as e:
            st.error(f"Error connecting to API: {e}")
