#Python Program to generate 1 to N Prime numbers
N = int(input("Enter the number: "))
print(f"The Prime Numbers b/w 1 to {N} are: ")
for i in range(2, N+1):
        flag=True
        for j in range(2, i):
          if i % j == 0:
            flag=False
            break
        if flag == True:
            print(i,end=" ")
