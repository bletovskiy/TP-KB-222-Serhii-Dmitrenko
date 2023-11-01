from operations import calculatorOperations

while True:
    print("Add = '+' \nSubtract = '-'\nMultiply = '*'\nDivide = '/'\nExit = 'Q' or 'q")
    
    operation = input("Enter operation: ")
    
    if operation in ["Q", "q"]:
        break
    
    calculator = calculatorOperations()
    a = calculator.getInt("Enter number 'a': ")
    b = calculator.getInt("Enter number 'b': ")
    
    result = calculator.performOperation(operation, a, b)
    print(f"Result: {result}\n")
    calculator.logToFile(operation, a, b, result)
