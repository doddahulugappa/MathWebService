# MathWebService Rest API using FatAPI

## This API designed to solve below maths problems
- Nth Fibonacci Number
- Factorial of a given Number
- Ackermann Function

## Requirements

* Python >= 3.6 (tested under Python 3.9.6)

## Setting up project
`cd MathWebService`

`python -m venv venv` optional

`venv\Scripts\activate` optional

`pip install -r requirements.txt`

execute `pytest` to test the API

execute `uvicorn app.main:app --reload` to run the API

[Click here to explore all API endpoints](http://localhost:8000/docs)

# Serverless FastAPI with AWS Lambda
```
pip install mangum
```

## Setup AWS Resources
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

# Docker
## Build Docker image
`cd MathWebService`

`docker build -t mathwebservice .`
## Run Docker Image
`docker run -it -p 8000:8000 mathwebservice`


