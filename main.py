from functools import reduce

from fastapi import FastAPI

app = FastAPI()

@app.get("/fibonacci/{n}")
async def get_nth_fibonacci(n:int):
    a,b=0,1 #initial fibonacci numbers
    for i in range(n):
        a,b = b,a+b
    return {str(n)+"Th Fibonacci Number":a}

@app.get("/factorial/{n}")
async def get_factorial(n:int):
    factorial = reduce(lambda x, y: x * y, range(1,n+1))

    return {"Th Factorial of "+str(n):factorial}



def ackermann(m, n):
    """
    Ackermann solution
    :param m:
    :param n:
    :return: solution
    """
    if m == 0:
        return (n + 1)
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

@app.get("/ackermann/")
async def solve_ackermann(m:int = 0, n:int =1):

    return {"Th Ackermann Solution":ackermann(m, n)}