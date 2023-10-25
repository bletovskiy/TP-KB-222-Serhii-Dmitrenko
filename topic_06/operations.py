from functions import *

def getInt(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            logToFile("Invalid input", "", "", "Invalid input. Please enter a valid integer.")

def getOperation(valid_operations):
    while True:
        operation = input("Enter operation: ")
        if operation in valid_operations:
            return operation
        else:
            print("Invalid operation. Please enter a valid operation.")
            logToFile("Invalid operation", "Null", "Null", "Invalid input")

valid_operations = ['+', '-', '*', '/', 'Q', 'q']