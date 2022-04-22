from functools import reduce
from fastapi import FastAPI

import logging
import logging.handlers as handlers

import timeit

logger = logging.getLogger('main_app')
logger.setLevel(logging.INFO)

# Here we define our formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logHandler = handlers.RotatingFileHandler('api_app.log', maxBytes=10*1024,  backupCount=2)
logHandler.setLevel(logging.INFO)

# Here we set our logHandler's formatter
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

app = FastAPI()


@app.get("/fibonacci/{number}")
async def get_nth_fibonacci_number(number: int):
    """
    returns nth fibonacci number
    """
    start = timeit.default_timer()
    if number < 0:
        return {"Message": "Invalid Input"}
    a, b = 0, 1  # Initial first fibonacci numbers
    for i in range(number):
        a, b = b, a+b
    fibonacci_no = a
    stop = timeit.default_timer()
    logger.info(get_nth_fibonacci_number.__name__+" Called")
    logger.info("Input: " + str(number))
    logger.info("Output:" + str(fibonacci_no))
    logger.info("Time Taken(in seconds):" + str(stop - start))
    ord_value = ordinal(number)  # get the ordinal of number
    message = {ord_value+" Fibonacci Number": fibonacci_no}
    return message


@app.get("/factorial/{n}")
async def get_factorial_of_given_number(n: int):
    """
    returns factorial of a given number
    """
    if n < 0:
        return {"Message": "Invalid Input"}

    if n == 0 or n == 1:
        factorial = 1
    else:
        # starts multiply by 1 to till N and saves cumulative product
        factorial = reduce(lambda x, y: x * y, range(1, n+1))
    message = {"Factorial of " + str(n): factorial}
    return message


@app.get("/ackermann/")
async def solve_ackermann(m: int = 0, n: int = 1):
    """
    Ackermann solution
    :param m:
    :param n:
    :return: solution
    """
    try:
        solution = ackermann(m, n)
    except Exception as e:
        print(e)
        solution = "Maximum recursion depth exceeded in comparison, Try M smaller number"
    return {"Ackermann Solution": solution}


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
