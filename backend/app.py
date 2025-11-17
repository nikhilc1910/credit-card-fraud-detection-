from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request model
class Transaction(BaseModel):
    step: int
    types: int
    amount: float
    oldbalanceorig: float
    newbalanceorig: float
    oldbalancedest: float
    newbalancedest: float
    isflaggedfraud: int

# Load model once
model = joblib.load("credit_fraud.pkl")

@app.get("/")
def home():
    return {"status": "backend working"}

@app.post("/predict/")
def predict(data: Transaction):

    features = np.array([[
        data.step,
        data.types,
        data.amount,
        data.oldbalanceorig,
        data.newbalanceorig,
        data.oldbalancedest,
        data.newbalancedest,
        data.isflaggedfraud,
    ]])

    result = model.predict(features)[0]
    return {"prediction": int(result)}
