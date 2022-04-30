import os
from functools import reduce
from fastapi import FastAPI, Body, Depends
from fastapi.responses import JSONResponse
import hashlib

import logging
import logging.handlers as handlers

import timeit

from app.model import UserSchema, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import sign_jwt
from app.database.dboperation import connect_db, close_db_conn

logger = logging.getLogger('main_app')
logger.setLevel(logging.INFO)

LOG_FILE = 'api_app.log'
# Here we define our formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logHandler = handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=2)  # 1 MB
logHandler.setLevel(logging.INFO)

# Here we set our logHandler's formatter
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

app = FastAPI()


@app.get("/fibonacci/{number}", dependencies=[Depends(JWTBearer())], tags=["maths"])
async def get_nth_fibonacci_number(number: int):
    """
    returns nth fibonacci number
    """
    if number < 0:
        message = {"Message": "Invalid Input"}
        format_log = "Endpoint: Fibonacci - Input: {} - Output: Invalid Input".format(number)
        logger.warning(format_log)
        return JSONResponse(message)
    start = timeit.default_timer()
    a, b = 0, 1  # Initial first fibonacci numbers
    for i in range(number):
        a, b = b, a+b
    fibonacci_no = a
    stop = timeit.default_timer()
    format_log = "Endpoint: Fibonacci - Input: {} - Output: {} - Time Taken(in seconds): {}" \
                 "".format(number, fibonacci_no, stop - start)
    logger.info(format_log)
    ord_value = ordinal(number)  # get the ordinal of number
    message = {"{} Fibonacci Number".format(ord_value): fibonacci_no}
    return JSONResponse(message)


@app.get("/factorial/{number}", dependencies=[Depends(JWTBearer())], tags=["maths"])
async def get_factorial_of_given_number(number: int):
    """
    returns factorial of a given number
    """
    if number < 0:
        message = {"Message": "Invalid Input"}
        format_log = "Endpoint: Factorial - Input: {} - Output: Invalid Input".format(number)
        logger.warning(format_log)
        return JSONResponse(message)

    start = timeit.default_timer()
    if number == 0 or number == 1:
        factorial = 1
    else:
        # starts multiply by 1 to till N and saves cumulative product
        factorial = reduce(lambda x, y: x * y, range(1, number+1))

    stop = timeit.default_timer()
    format_log = "Endpoint: Factorial - Input: {} - Output: {} - Time Taken(in seconds): {}" \
                 "".format(number, factorial, stop - start)
    logger.info(format_log)

    message = {"Factorial of {}".format(number): factorial}
    return JSONResponse(message)


@app.get("/ackermann/", dependencies=[Depends(JWTBearer())], tags=["maths"])
async def solve_ackermann(m: int = 0, n: int = 1):
    """
    Ackermann solution
    :param m:
    :param n:
    :return: solution
    """
    start = timeit.default_timer()
    try:
        solution = ackermann(m, n)
    except Exception as e:
        print(e)
        solution = "Maximum recursion depth exceeded in comparison, Try M smaller number"

    stop = timeit.default_timer()
    format_log = "Endpoint: Ackermann - Input: M={},N={} - Output: {} - Time Taken(in seconds): {}" \
                 "".format(m, n, solution, stop - start)
    logger.info(format_log)
    message = {"Ackermann Solution": solution}
    return JSONResponse(message)


@app.get("/logs/", dependencies=[Depends(JWTBearer())], tags=["logs"])
async def get_logs():
    log_list = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as of:  # Open log file in read mode
            logs = of.readlines()  # Read all the lines

        for line in logs:
            logs_dict = {}
            time, message_type, *messages = line.split(" - ")
            logs_dict["time"] = time
            logs_dict["log_type"] = message_type
            for message in messages:
                key, value = message.split(":")
                value = value.strip()  # stripe out space if any
                logs_dict[key] = int(value) if value.isnumeric() else value  # convert to number

            log_list.append(logs_dict)
    return JSONResponse(log_list)


def ackermann(m, n):
    """
    Ackermann solution
    :param m:
    :param n:
    :return: solution
    """
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


def ordinal(value):
    """
    input: takes number
    return: ordinal_number
    """
    if value % 100//10 != 1:
        if value % 10 == 1:
            ordinal_value = u"%d%s" % (value, "st")
        elif value % 10 == 2:
            ordinal_value = u"%d%s" % (value, "nd")
        elif value % 10 == 3:
            ordinal_value = u"%d%s" % (value, "rd")
        else:
            ordinal_value = u"%d%s" % (value, "th")
    else:
        ordinal_value = u"%d%s" % (value, "th")

    return ordinal_value


def check_user(data: UserLoginSchema):
    conn = connect_db()
    cur = conn.cursor()
    query = "select * from user"
    cur.execute(query)
    users = cur.fetchall()
    close_db_conn(conn)
    hashed_password = hashlib.sha256(data.password.encode('utf-8')).hexdigest()
    for user in users:
        if user[2] == data.email and user[3] == hashed_password:
            return True
    return False


@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    conn = connect_db()
    cur = conn.cursor()
    query = "select * from user"
    cur.execute(query)
    total_rec = len(cur.fetchall())
    hashed_password = hashlib.sha256(user.password.encode('utf-8')).hexdigest()
    query = "insert into user values("+str(total_rec+1)+",'"+user.fullname+"','"+user.email+"','"+hashed_password+"')"
    cur.execute(query)
    conn.commit()
    close_db_conn(conn)
    return sign_jwt(user.email)


@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return sign_jwt(user.email)
    return {
        "error": "Wrong login details!"
    }
