#Python Program to find reverse of a given number
n = int(input("Enter a number: "))
temp = n
rev = 0
while n!=0:
    d = n % 10
    rev = rev * 10 + d
    n = n // 10
print(f"Reverse of number {temp} is: {rev}")