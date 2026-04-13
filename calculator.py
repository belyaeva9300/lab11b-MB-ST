"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    pass

def add(a, b):
    pass

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Log args")
    return math.log(b, a)


