from functools import reduce
from fastapi import FastAPI
from fastapi.responses import JSONResponse

import logging
import logging.handlers as handlers

import timeit

logger = logging.getLogger('main_app')
logger.setLevel(logging.INFO)

# Here we define our formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logHandler = handlers.RotatingFileHandler('../api_app.log', maxBytes=10 * 1024, backupCount=2)
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
    if number < 0:
        message = {"Message": "Invalid Input"}
        return JSONResponse(message)
    start = timeit.default_timer()
    a, b = 0, 1  # Initial first fibonacci numbers
    for i in range(number):
        a, b = b, a+b
    fibonacci_no = a
    stop = timeit.default_timer()
    logger.info(get_nth_fibonacci_number.__name__+" Called")
    logger.info("Input: {}".format(number))
    logger.info("Output: {}".format(fibonacci_no))
    logger.info("Time Taken(in seconds): {}".format(stop - start))
    ord_value = ordinal(number)  # get the ordinal of number
    message = {"{} Fibonacci Number".format(ord_value): fibonacci_no}
    return JSONResponse(message)


@app.get("/factorial/{number}")
async def get_factorial_of_given_number(number: int):
    """
    returns factorial of a given number
    """
    if number < 0:
        message = {"Message": "Invalid Input"}
        return JSONResponse(message)

    start = timeit.default_timer()
    if number == 0 or number == 1:
        factorial = 1
    else:
        # starts multiply by 1 to till N and saves cumulative product
        factorial = reduce(lambda x, y: x * y, range(1, number+1))

    stop = timeit.default_timer()
    logger.info(get_factorial_of_given_number.__name__ + " Called")
    logger.info("Input: {}".format(number))
    logger.info("Output: {}".format(factorial))
    logger.info("Time Taken(in seconds): {}".format(stop - start))

    message = {"Factorial of {}".format(number): factorial}
    return JSONResponse(message)


@app.get("/ackermann/")
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
    logger.info(solve_ackermann.__name__ + " Called")
    logger.info("Input: {},{}".format(m, n))
    logger.info("Output: {}".format(solution))
    logger.info("Time Taken(in seconds): {}".format(stop - start))
    message = {"Ackermann Solution": solution}
    return JSONResponse(message)


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
