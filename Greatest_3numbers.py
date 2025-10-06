#Python Program to find greatest among three numbers
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
c=int(input("Enter c value: "))
if a>b and a>c :
   print(f"{a} is greater among three numbers")
elif b>a and b>c :
   print(f"{b} is greater among three numbers")
else :
   print(f"{c} is greater among three numbers")