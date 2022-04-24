from fastapi.testclient import TestClient
from app.main import app, ordinal

client = TestClient(app)

def test_fibonacci():
    number = 4
    ord_value = ordinal(number)
    response = client.get("/fibonacci/"+str(number))
    assert response.status_code == 200
    assert response.json() == {ord_value+" Fibonacci Number": 3}


def test_fibonacci_non_negative():
    response = client.get("/fibonacci/-4")
    assert response.status_code == 200
    assert response.json() == {"Message": "Invalid Input"}


def test_factorial():
    number = 4
    response = client.get("/factorial/"+str(number))
    assert response.status_code == 200
    assert response.json() == {"Factorial of "+str(number): 24}


def test_factorial_non_negative():
    number = -1
    response = client.get("/factorial/"+str(number))
    assert response.status_code == 200
    assert response.json() == {"Message": "Invalid Input"}


def test_ackermann():
    response = client.get("/ackermann/?m=0&n=1")
    assert response.status_code == 200
    assert response.json() == {"Ackermann Solution": 2}

def test_root():
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}