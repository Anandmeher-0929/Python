#Python Program to consider age and find their status
"""
age > 60 - senior citizen
age 25 to 59 - Working citizen
age 16 to 24 - College Students
age 4 to 15 - School Kids
age 1 to 3 - Play kids
"""
age = int(input("Enter age: "))
if age >= 60 : 
    print("Age is Older than 60 years i.e., Senior Citizen")
elif 25 <= age <= 59 :
    print("Age is in between 25 to 59 years i.e., Working Citizen")
elif 16 <= age <= 24 :
    print("Age is in between 16 to 24 years i.e., College Students")
elif 4 <= age <= 15 :
    print("Age is in between 4 to 15 years i.e., School Kids")
elif 1 <= age <= 3 :
    print("Age is in between 1 to 3 years i.e., Play Kids")
else :
    print("Invalid")