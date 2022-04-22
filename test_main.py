from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_fibonacci():
    number = 4
    response = client.get("/fibonacci/"+str(number))
    assert response.status_code == 200
    assert response.json() == {str(number)+"Th Fibonacci Number": 3}

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

