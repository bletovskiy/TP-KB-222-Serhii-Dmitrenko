import datetime
import os
logFile = "log.txt"
dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(dir, "log.txt")


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
    
def logToFile(operation, a, b, result):
    date = datetime.datetime.now()
    formatDate = date.strftime("%Y-%m-%d %H:%M:%S")

    logEntry = f"{formatDate}: Operation: {operation}, a: {a}, b: {b}, Result: {result}"

    with open(path, "a") as file:
        file.write(logEntry + "\n")

