#Python Program to swap two variables with temporary variables
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
print("Before Swapping two variables...")
print("--------------------------------")
print(f"a value is {a}")
print(f"b value is {b}")
t=a
a=b
b=t
print("After Swapping two variables...")
print("--------------------------------")
print(f"a value is {a}")
print(f"b value is {b}")

