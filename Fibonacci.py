#Python Program to generate the Fibonacci Series
N = int(input("Enter the number: "))
f1 = 1
f2 = 1
print(f"The First {N} Fibonacci series: ")
print(f1,end=" ")
print(f2,end=" ")
for i in range(1,N-1):
    f3 = f1 + f2
    print(f3,end=" ")
    f1 = f2
    f2 = f3