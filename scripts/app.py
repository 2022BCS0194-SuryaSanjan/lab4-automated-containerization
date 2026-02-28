from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load model
model = joblib.load("outputs/results/model.pkl")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(features: dict):
    data = np.array([list(features.values())])
    prediction = model.predict(data)
    return {"prediction": float(prediction[0])}