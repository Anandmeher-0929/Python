#Python program to calculate simple interest
P=float(input("Enter Principle amount:"))
T=float(input("Enter Time:"))
R=float(input("Enter Rate:"))
SI = ( P * T * R ) / 100
print(f"The Simple Interest is {SI:.2f}")