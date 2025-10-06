#Python Program to find roots of Quadratic Equation
from math import *
a,b,c = [int (x) for x in input("Enter values of a,b,c: ").split()]
D = (b**2 - (4 * a * c))
if D > 0:
    print("Roots are real and distinct.")
    r1 = (-b + sqrt(D)) / (2.0 * a)
    r2 = (-b - sqrt(D)) / (2.0 * a)
elif D < 0:
    print("Roots are imaginary.")
else :
    print("Roots are real and equal.")
    r1 = -b / (2.0 * a)
    r2 = -b / (2.0 * a)
    print(f"Root 1 is {r1}.")
    print(f"Root 2 is {r2}.")