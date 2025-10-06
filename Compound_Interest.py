# Python Program to calculate Compound Interest
Principle= float(input("Enter Principle Value:"))
Rate=float(input("Enter rate:"))
Compounded_Value = float(input("Enter Compounded Value per year:"))
Time=float(input("Enter Time:"))
#Compound Interest Formula
Amount=Principle*pow((1+Rate/Compounded_Value),Time)
C=float(Amount - Principle)
print(f"Compound Interest for {Time:} year(s) is {C:.2f}")