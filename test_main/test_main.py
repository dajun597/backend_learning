from fastapi.testclient import TestClient
from app.main import app
from app.database import delete_application

client = TestClient(app)
def test_main_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()['status']=="OK"

def test_create_application():
    response = client.post("/calculate-ltv", json={
        "customer_id": "C001",
        "property_value": 500000,
        "existing_mortgage": 200000,
        "loan_amount": 50000
    })

    assert response.status_code == 200
    data = response.json()
    assert data["customer_id"] == "C001"
    assert data["ltv"] == 0.5
    assert "application_id" in data
    delete_application(data["application_id"])


