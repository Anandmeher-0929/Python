#Python Program to print following pattern
"""
* * * *
*     *
* * * *
*     *
*     *
"""
rows = int(input("Enter number of rows: "))
for i in range(1,rows+2):
    for j in range(1,rows+1):
        if(i==1 or i==rows-1) or (j==1 or j==rows):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()