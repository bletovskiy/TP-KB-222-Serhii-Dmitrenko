from functions import calculatorFunctions

class calculatorOperations:
    def __init__(self):
        self.valid_operations = ['+', '-', '*', '/', 'Q', 'q']
        self.functions = calculatorFunctions()

    def getInt(self, prompt):
        return self.functions.getInt(prompt)

    def performOperation(self, operation, a, b):
        return self.functions.performOperation(operation, a, b)

    def logToFile(self, operation, a, b, result):
        self.functions.logToFile(operation, a, b, result)
