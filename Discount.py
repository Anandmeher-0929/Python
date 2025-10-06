#Python Program to calculate the discount in the mall
amount = float(input("Enter amount: "))
discount = int(input("Enter discount : "))
price = (amount * discount) / 100
totalamount = amount - price
print(f"Total amount for {amount} after applied {discount}% discount is {totalamount}")