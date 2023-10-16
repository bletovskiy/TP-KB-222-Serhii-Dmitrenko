def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero is not allowed"