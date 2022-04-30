from fastapi.testclient import TestClient
from app.main import app, ordinal

client = TestClient(app)

NUMBER = 4
headers = {'Authorization': None}
user = {"email": "puli@huli.com", "password": "Puli434532"}


def test_signup():
    user["fullname"] = "Doddahulugappa Barikara"
    response = client.post("/user/signup", json=user)
    assert response.status_code == 200
    token = response.json()["access_token"]
    headers['Authorization'] = 'Bearer '+token


def test_login():
    response = client.post("/user/login", json=user)
    assert response.status_code == 200
    token = response.json()["access_token"]
    headers['Authorization'] = 'Bearer '+token


def test_fibonacci():
    number = NUMBER
    ord_value = ordinal(number)
    response = client.get("/fibonacci/"+str(number), headers=headers)
    assert response.status_code == 200
    assert response.json() == {ord_value+" Fibonacci Number": 3}


def test_fibonacci_non_negative():
    response = client.get("/fibonacci/-4", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"Message": "Invalid Input"}


def test_factorial():
    number = NUMBER
    response = client.get("/factorial/"+str(number), headers=headers)
    assert response.status_code == 200
    assert response.json() == {"Factorial of "+str(number): 24}


def test_factorial_non_negative():
    number = -1
    response = client.get("/factorial/"+str(number), headers=headers)
    assert response.status_code == 200
    assert response.json() == {"Message": "Invalid Input"}


def test_ackermann():
    response = client.get("/ackermann/?m=0&n=1", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"Ackermann Solution": 2}


def test_root():
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
