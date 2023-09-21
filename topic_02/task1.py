import math

def Disc(a,b,c):
    D = b**2 - 4 * a * c
    return D

def Roots(a,b,c):
    D = Disc(a, b, c)

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return x1, x2
    elif D == 0:
        x1 = -b / (2 * a)
        return x1
    else:
        return None
    
a, b, c = map(float, input("Enter a, b and c (separated by spaces): ").split())

roots = Roots(a, b, c)
if roots is not None:
    if isinstance(roots, tuple):
        x1, x2 = roots
        print("Two real roots:")
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")
    else:
        x1 = roots
        print("One real root: x1 = ", x1)
else:
    print("No real roots")