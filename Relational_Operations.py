#Python Program to implement Relational Operations
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
if  a>b :
    print(f"{a} is greater than {b}")
elif  a<b :
    print(f"{a} is lesser than {b}")
elif  a==b :
    print(f"{a} is equal to {b}")
elif  a>=b :
    print(f"{a} is greater than and equal to {b}")
elif  a<=b :
    print(f"{a} is lesser than and equal to {b}")
else  :
    print(f"{a} is not equal to {b}")
