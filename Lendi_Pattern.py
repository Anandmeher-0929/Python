N = input("Enter the string: ")
temp = len(N)
for i in range(temp):
    for j in range(temp-i-1):
            print(" ",end= " ")
    for j in range(i+1):
            print(N[j],end=" ")
    for j in range(i):
            print(N[i-j-1],end=" ")
    print()
    