#Python Program to print set of Odd numbers between 1 to N
N=int(input("Enter N value: "))
i=1
while i<=N :
    if i % 2 !=0 :
        print(i,end = " ")
    i = i+1
