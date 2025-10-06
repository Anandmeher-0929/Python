# Python program to swap two variables without temporary variable
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
print("Before Swapping two variables...")
print("--------------------------------")
print(f"a value is {a}")
print(f"b value is {b}")
a=a+b
b=a-b
a=a-b
print("After Swapping two variables...")
print("--------------------------------")
print(f"a value is {a}")
print(f"b value is {b}")
