import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Credit Card Fraud Detection Web App", layout="wide")

st.title("Credit Card Fraud Detection Web App")
st.image("image.png")

# Load the model
@st.cache_resource
def load_model():
    return joblib.load("credit_fraud.pkl")

model = load_model()


st.write("""
## About
This Streamlit app predicts **fraudulent credit card transactions** using a machine learning model.

Enter the transaction details on the left and click **Detection Result** to see if the transaction is fraudulent.
""")

# Sidebar inputs
st.sidebar.header("Input Features of The Transaction")

sender_name = st.sidebar.text_input("Input Sender ID")
receiver_name = st.sidebar.text_input("Input Receiver ID")
step = st.sidebar.slider("Number of Hours it took to complete:", 0, 100, 0)

st.sidebar.write("""
### Enter Type of Transfer:
0 = Cash In  
1 = Cash Out  
2 = Debit  
3 = Payment  
4 = Transfer  
""")

types = st.sidebar.selectbox("Transaction Type", (0, 1, 2, 3, 4))

amount = st.sidebar.number_input("Amount in $", min_value=0, max_value=500000)
oldbalanceorg = st.sidebar.number_input("Sender Balance Before Transaction", min_value=0, max_value=500000)
newbalanceorg = st.sidebar.number_input("Sender Balance After Transaction", min_value=0, max_value=500000)
oldbalancedest = st.sidebar.number_input("Recipient Balance Before Transaction", min_value=0, max_value=500000)
newbalancedest = st.sidebar.number_input("Recipient Balance After Transaction", min_value=0, max_value=500000)

isflaggedfraud = 1 if amount >= 200000 else 0

# Prediction button
if st.button("Detection Result"):

    if sender_name == "" or receiver_name == "":
        st.error("Please enter Sender ID and Receiver ID!")
    else:
        features = np.array([[step, types, amount, oldbalanceorg, newbalanceorg,
                              oldbalancedest, newbalancedest, isflaggedfraud]])

        prediction = model.predict(features)[0]

        result = "Fraudulent ❌" if prediction == 1 else "Legitimate ✅"

        st.subheader("Prediction Result")
        st.write(f"**The transaction between `{sender_name}` and `{receiver_name}` is:**")
        st.success(result) if prediction == 0 else st.error(result)
