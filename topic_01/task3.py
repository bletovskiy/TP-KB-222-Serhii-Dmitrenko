def calculate_discriminant(a, b, c):
    D = b**2 - 4*a*c
    return D

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

print(calculate_discriminant(a, b, c))