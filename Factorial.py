#Python Program to find factorial of a given number
N = int(input("Enter the number: "))
fact = 1
for i in range(1, N+1):
    fact = fact * i
print(f"The factorial of {N} is {fact}")