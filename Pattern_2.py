#Python program to print following pattern
"""
1
22
333
4444
55555
"""
rows = int(input("Enter the number of rows: "))
for row in range(1,rows+1):
    for col in range(1,row+1):
        print(row,end=" ")
    print()