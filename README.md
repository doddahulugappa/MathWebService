# MathWebService Rest API using FatAPI

## This API designed to solve below maths problems
- Nth Fibonacci Number
- Factorial of a given Number
- Ackermann Function

## Setting up project
`cd MathWebService`

`pip install -r requirements.txt`

`cd app`

`pytest test_main.py`

`uvicorn main:app --reload`

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


