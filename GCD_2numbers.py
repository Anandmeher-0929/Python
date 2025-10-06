#Python Program to find GCD of two numbers
m,n = [int(x) for x in input("Enter two values: ").split()]
a,b = m,n
if n>m:
    m,n = n,m
while n!=0:
    temp = m
    m=n
    n = temp % n
print(f"The GCD of {a} and {b} is {m}")