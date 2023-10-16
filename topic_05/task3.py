from functions import *
from operations import *

while True:
    print("Add = '+' \nSubtract = '-'\nMultiply = '*'\nDivide = '/'\nExit = 'Q' or 'q'")
    
    operation = getOperation(valid_operations)

    if operation == "Q" or operation == "q":
        break
    else:
        a = getInt("Enter number 'a': ")
        b = getInt("Enter number 'b': ")
        
        match operation:
            case "+":
                print(f"Result: {add(a, b)}\n")
            case "-":
                print(f"Result: {subtract(a, b)}\n")
            case "*":
                print(f"Result: {multiply(a, b)}\n")
            case "/":
                print(f"Result: {divide(a, b)}\n")