from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("credit_fraud.pkl")

@app.get("/")
def home():
    return {"status": "backend working"}

@app.post("/predict/")
def predict(data: dict):

    features = np.array([[
        data.get("step"),
        data.get("types"),
        data.get("amount"),
        data.get("oldbalanceorig"),
        data.get("newbalanceorig"),
        data.get("oldbalancedest"),
        data.get("newbalancedest"),
        data.get("isflaggedfraud"),
    ]])

    result = model.predict(features)[0]
    return {"prediction": int(result)}
