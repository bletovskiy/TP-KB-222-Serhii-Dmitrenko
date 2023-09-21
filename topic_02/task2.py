def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

a, b = map(float, input("Enter number 'a' and 'b' (separated by spaces): ").split())
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = add(a, b)
elif operation == "-":
    result = substract(a, b)
elif operation == "*":
    result = multiply(a, b)
elif operation == "/":
    result = divide(a, b)
else: 
    result = "Invalid operation"

print(f"Result: {result}")