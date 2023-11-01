import datetime
import os

class calculatorFunctions:
    def getInt(self, prompt):
        while True:
            try:
                num = int(input(prompt))
                return num
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                self.logToFile("Invalid input", "", "", "Invalid input. Please enter a valid integer.")

    def performOperation(self, operation, a, b):
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            try:
                result = a / b
                return result
            except ZeroDivisionError:
                return "Division by zero is not allowed"

    def logToFile(self, operation, a, b, result):
        logFile = "log.txt"
        dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(dir, "log.txt")

        date = datetime.datetime.now()
        formatDate = date.strftime("%Y-%m-%d %H:%M:%S")

        logEntry = f"{formatDate}: Operation: {operation}, a: {a}, b: {b}, Result: {result}"

        with open(path, "a") as file:
            file.write(logEntry + "\n")
