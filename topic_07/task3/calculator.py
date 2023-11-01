from operations import calculatorOperations

while True:
    print("Add = '+' \nSubtract = '-'\nMultiply = '*'\nDivide = '/'\nExit = 'Q' or 'q")
    
    calculator = calculatorOperations()
    operation = calculator.getValidOperation()

    if operation in ["Q", "q"]:
        break

    a = calculator.getInt("Enter number 'a': ")
    b = calculator.getInt("Enter number 'b': ")
    
    result = calculator.performOperation(operation, a, b)
    print(f"Result: {result}\n")
    calculator.logToFile(operation, a, b, result)
