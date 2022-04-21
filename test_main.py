from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_fibonacci():
    response = client.get("/fibonacci/4")
    assert response.status_code == 200
    assert response.json() == {"4Th Fibonacci Number": 3}

def test_factorial():
    response = client.get("/factorial/4")
    assert response.status_code == 200
    assert response.json() == {"Factorial of 4": 24}

def test_ackermann():
    response = client.get("/ackermann/?m=0&n=1")
    assert response.status_code == 200
    assert response.json() == {"Ackermann Solution": 2}

