# MathWebService Rest API using FatAPI

## This API designed to solve below maths problems
- Nth Fibonacci Number
- Factorial of a given Number
- Ackermann Function

## Requirements

* Python >= 3.6 (tested under Python 3.9.6 & 3.10.4)

## Setting up project
 - Unzip the file

 - Open the cmd

 - `cd Python-assessment-DB-04-25-2022)`(to unzipped folder)

 - `cd MathWebService`(to project folder)
### Create Virtual env and activate
 - `python -m venv venv` optional (to create virtualenv)

 - `venv\Scripts\activate` optional (to activate virtualenv)

### Install libraries 
 - `pip install -r requirements.txt`
 
### Create database and tables
 - `python app\database\dboperation.py`

### Execute tests
 - execute `pytest` to test the API

### Run webserver
 - execute `uvicorn app.main:app --reload` to run the API

### Open the below url
 - [Click here to explore all API endpoints](http://localhost:8000/docs)

## Serverless FastAPI with AWS Lambda
```
pip install mangum
```

### Setup AWS Resources
- Create S3 Bucket
- Upload Zip File
- Package Lambda
- Upload Zip File to S3
- Create AWS Lambda
- Update Handler
- Test FastAPI Lambda
- Create API Gateway
- Choose the Protocol
- Create Root Proxy Method
- Create Resource
- Deploy Lambda Proxy API

## Docker
### Build Docker image
`cd MathWebService`

`docker build -t mathwebservice .`
### Run Docker Image
`docker run -it -p 8000:8000 mathwebservice`


## JWT Authentication
`pip install PyJWT python-decouple`

## User Registration and Login
`pip install "pydantic[email]"`


