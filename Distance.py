#Python program to find distance between two points
from math import *
x1,y1 = [int (x) for x in input("Enter A coordinates:").split()]
x2,y2 = [int (x) for x in input("Enter B coordinates:").split()]
distance = sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"The distance b/w A({x1},{y1}) and B({x2},{y2}) is {distance:.4f}")