# Python Program to find sum of first N natural numbers
N = int(input("Enter a Number: "))
sum = 0
i = 1
while i <= N:
    sum = sum + i
    i += 1
print(f"The sum of first {N} natural numbers is: {sum}")

