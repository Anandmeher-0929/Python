#Python Program to print 5 multiples b/w 1 to N using for with else
N = int(input("Enter N value: "))
for i in range(5,N+1,5):
    print(i,end=" ")
else :
    print("Goodbye")