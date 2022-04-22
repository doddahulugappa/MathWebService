from functools import reduce
from fastapi import FastAPI

app = FastAPI()


@app.get("/fibonacci/{n}")
async def get_nth_fibonacci_number(n: int):
    """
    returns nth fibonacci number
    """
    if n < 0:
        return {"Message": "Invalid Input"}
    a, b = 0, 1  # Initial first fibonacci numbers
    for i in range(n):
        a, b = b, a+b

    ord_value = ordinal(n)  # get the ordinal of number
    message = {ord_value+" Fibonacci Number": a}
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
