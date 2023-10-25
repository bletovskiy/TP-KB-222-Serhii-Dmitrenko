from functions import *
from operations import *


while True:
    print("Add = '+' \nSubtract = '-'\nMultiply = '*'\nDivide = '/'\nExit = 'Q' or 'q'")
    
    operation = getOperation(valid_operations)

    if operation == "Q" or operation == "q":
        logToFile(operation, "Null", "Null", "Exit")
        break
    else:
        a = getInt("Enter number 'a': ")
        b = getInt("Enter number 'b': ")
        
        match operation:
            case "+":
                result = add(a, b)
                print(f"Result: {result}\n")
            case "-":
                result = subtract(a, b)
                print(f"Result: {result}\n")
            case "*":
                result = multiply(a, b)
                print(f"Result: {result}\n")
            case "/":
                result = divide(a, b)
                print(f"Result: {result}\n")
          

        logToFile(operation, a, b, result)