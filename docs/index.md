# MathWebService Rest API using FatAPI

## This API is designed to solve below maths problems
- Nth Fibonacci Number
- Factorial of a given Number
- Ackermann Function

## Requirements

* Python >= 3.6 (tested under Python 3.9.6 & 3.10.4)

## Setting up project
 - Open the cmd

 - `git clone https://github.com/doddahulugappa/MathWebService.git`

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

### Open below url and exlpore
 - http://\<HOST\>:\<PORT\>/docs

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


## Documentation
This API is using basic authentication and jwt token authorization.
Firstly we will have to signup to get the jwt token which is valid for 5 minutes
and use the token as authorization to call other API endpoints. If already signed up,
we just need to signin to get the jwt token.

