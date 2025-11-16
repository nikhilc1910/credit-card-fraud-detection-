from fastapi import FastAPI
import joblib
import uvicorn
import numpy as np
import os

app = FastAPI(title="Credit Card Fraud Detection API")

# Load Model
model = joblib.load("credit_fraud.pkl")

@app.get("/")
def home():
    return {"message": "Backend is running!"}

@app.post("/predict/")
def predict(data: dict):

    features = np.array([[
        data["step"],
        data["types"],
        data["amount"],
        data["oldbalanceorig"],
        data["newbalanceorig"],
        data["oldbalancedest"],
        data["newbalancedest"],
        data["isflaggedfraud"]
    ]])

    prediction = model.predict(features)[0]

    return {"prediction": int(prediction)}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
