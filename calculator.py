"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/belyaeva9300/lab11b-MB-ST.git
# Partner 1: Masha Belyaeva
# Partner 2: Sebastian Tejada

import math
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid input for logarithm")
    return math.log(b, a)

def exp(a, b):
    return a ** b

