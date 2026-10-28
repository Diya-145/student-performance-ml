
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

MODEL_PATH = Path(__file__).parent / "model.joblib"
model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="Student Performance Prediction API"
)


class StudentInput(BaseModel):
    gender: str
    race_ethnicity: str
    parental_education: str
    lunch: str
    test_preparation: str
    reading_score: float = Field(ge=0, le=100)
    writing_score: float = Field(ge=0, le=100)


@app.get("/")
def home():
    return {"message": "Student Performance API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(student: StudentInput):
    data = pd.DataFrame([student.model_dump()])
    prediction = model.predict(data)[0]

    return {
        "predicted_math_score": round(float(prediction), 2)
    }
