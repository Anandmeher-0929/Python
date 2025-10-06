#Python program to print Math table
i = 1
tno = int(input("Enter table Number: "))
N = int(input("Enter the number : "))
while i<=N :
    r = tno * i
    print(f"{tno} * {i} = {r}")
    i +=1