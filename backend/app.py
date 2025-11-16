from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("credit_fraud.pkl")

@app.get("/")
def home():
    return {"status": "Backend up and running"}

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
        data["isflaggedfraud"],
    ]])

    prediction = int(model.predict(features)[0])
    
    return {"prediction": prediction}
