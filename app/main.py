from fastapi import FastAPI
import joblib
import pandas as pd
import os

from app.schema import CustomerInput

# Initialize API
app = FastAPI(title="CustIQ Churn Prediction API")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "rf_churn_model.pkl")

model = joblib.load(MODEL_PATH)


@app.get("/")
def home():
    return {"message": "CustIQ API is running"}


@app.post("/predict")
def predict_churn(customer: CustomerInput):

    data = pd.DataFrame([customer.dict()])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    return {
        "Churn Prediction": int(prediction),
        "Churn Probability": float(probability)
    }
