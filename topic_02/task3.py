def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

while True:
    print(f"Add = '+'")
    print(f"Substract = '-'")
    print(f"Multiply = '*'")
    print(f"Divide = '/'")
    print(f"Exit = ']'")
    operation = input("Enter operation : ")

    if operation == "]":
        break

    a, b = map(float, input("Enter number 'a' and 'b' (separated by spaces): ").split())
    
    match operation:
        case "+":
            print(add(a, b))
        case "-":
            print(substract(a, b))
        case "*":
            print(multiply(a, b))
        case "/":
            print(divide(a, b))
        case _:
            print("Invalid operation")

