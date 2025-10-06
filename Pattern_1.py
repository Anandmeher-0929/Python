#Python Program to print following pattern
"""
1
12
123
1234
12345
"""
rows = int(input("Enter the number of rows: "))
for row in range(1,rows+1):
    for col in range(1,row+1):
        print(col,end=" ")
    print()