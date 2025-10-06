#Python Program to simulate ATM function
amount = 0.0
deposit = 0.0
while(True) :
    print("1.Deposit\n2.Withdraw\n3.Exit\n")
    option = int(input("Enter your choice: "))
    if option == 1:
        deposit = float(input("Enter your deposit: "))
        amount = amount + deposit
        print(f"Your deposit amount is: {deposit}")
        print(f"Your amount is: {amount}")
    elif option == 2:
        if amount>10000:
            withdraw = float(input("Enter your withdrawal: "))
            amount = amount - withdraw
            print(f"Your withdrawal amount is: {withdraw}")
            print(f"Your amount is: {amount}")
    else:
        print("Invalid choice")
else:
    exit()
    