
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Student Performance API is running"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_prediction():
    payload = {
        "gender": "female",
        "race_ethnicity": "group B",
        "parental_education": "bachelor's degree",
        "lunch": "standard",
        "test_preparation": "completed",
        "reading_score": 85,
        "writing_score": 88
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert "predicted_math_score" in response.json()

    score = response.json()["predicted_math_score"]
    assert isinstance(score, (int, float))
    assert 0 <= score <= 100


def test_invalid_score():
    payload = {
        "gender": "female",
        "race_ethnicity": "group B",
        "parental_education": "bachelor's degree",
        "lunch": "standard",
        "test_preparation": "completed",
        "reading_score": 150,
        "writing_score": 88
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 422
