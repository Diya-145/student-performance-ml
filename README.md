
# Student Performance Prediction using Machine Learning

## Project Overview
This project predicts a student's math score using a trained
Random Forest Regression model.

The model is served through a FastAPI application and can be
tested locally or packaged using Docker. GitHub Actions
automatically runs tests and builds the Docker image.

## Dataset
Students Performance in Exams dataset from Kaggle:

https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Joblib
- FastAPI
- Pytest
- Docker
- GitHub Actions

## Model Training
The dataset is split into training and testing sets.
Categorical features are encoded, and a Random Forest
Regressor is trained to predict math scores.

Evaluation metrics include MAE, MSE, and R-squared.

## API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | / | Home endpoint |
| GET | /health | Health check |
| POST | /predict | Predict math score |

## Run Locally

Install dependencies:

    python -m pip install -r requirements.txt

Start the API:

    uvicorn app:app --reload

Open the API documentation:

http://127.0.0.1:8000/docs

## Run Automated Tests

    pytest -v

## Run with Docker

    docker build -t student-performance-api .
    docker run -p 8000:8000 student-performance-api

## Continuous Integration
GitHub Actions runs automated tests and builds the Docker
image when code is pushed to the main branch or a pull
request targets main.

## Model Artifact
The trained model is saved as model.joblib and loaded by
the FastAPI application.
