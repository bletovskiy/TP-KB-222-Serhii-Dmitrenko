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
    
def getInt(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def getOperation(valid_operations):
    while True:
        operation = input("Enter operation: ")
        if operation in valid_operations:
            return operation
        else:
            print("Invalid operation. Please enter a valid operation.")

valid_operations = ['+', '-', '*', '/', 'Q', 'q']

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