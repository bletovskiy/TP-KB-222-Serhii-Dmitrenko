def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b
    except ZeroDivisionError as exc:
        return str(exc)

def getInt(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter an integer.")

while True:
    print(f"Add = '+'")
    print(f"Subtract = '-'")
    print(f"Multiply = '*'")
    print(f"Divide = '/'")
    print(f"Exit = 'Q' or 'q'")
    operation = input("Enter operation: ")

    if operation == "Q" or "q":
        break

    a = getInt("Enter number 'a': ")
    b = getInt("Enter number 'b': ")

    try:
        result = None
        if operation == "+":
            result = add(a, b)
        elif operation == "-":
            result = substract(a, b)
        elif operation == "*":
            result = multiply(a, b)
        elif operation == "/":
            result = divide(a, b)
        else:
            print("Invalid operation")

        if result is not None:
            print(f"Result: {result}\n")

    except (ValueError, TypeError) as exc:
        print(f"Error: {exc}")