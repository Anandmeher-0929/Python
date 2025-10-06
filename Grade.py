#Python Program to declare the grade of the student using elif ladder
marks = float(input("Enter total marks of the Student: "))
if 100 >= marks >=90 :
    print("Student passed and secured S grade")
elif 89.9 >= marks >= 80 :
    print("Student passed and secured A grade")
elif 79.9 >= marks >= 70 :
    print("Student passed and secured B grade")
elif 69.9 >= marks >= 60 :
    print("Student passed and secured C grade")
elif 59.9 >= marks >= 50 :
    print("Student passed and secured D grade")
elif 49.9 >= marks >= 40 :
    print("Student passed and secured E grade")
elif 39.9 >= marks >= 0 :
    print("Student failed")
else :
    print("Invalid Marks")
