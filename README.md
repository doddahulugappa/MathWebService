# MathWebService Rest API using FatAPI

## This API designed to solve below maths problems
- Nth Fibonacci Number
- Factorial of a given Number
- Ackermann Function

## Setting up project
`cd MathWebService`

`pip install -r requirements.txt`

`pytest test_main.py`

`uvicorn main:app --reload`

[Open & Explore all API end points](http://localhost:8000/docs)

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
