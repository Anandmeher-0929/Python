# Python Program to demonstrate all operators
# Input values
a = 10
b = 3
print("=== Arithmetic Operators ===")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)   
print("a % b =", a % b)     
print("a ** b =", a ** b)   
print("\n=== Relational Operators ===")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print("\n=== Logical Operators ===")
print("(a > 5) and (b < 5):", (a > 5) and (b < 5))
print("(a > 5) or (b > 5):", (a > 5) or (b > 5))
print("not(a > b):", not(a > b))
print("\n=== Assignment Operators ===")
x = a   # Assign
print("x =", x)
x += b
print("x += b:", x)
x -= b
print("x -= b:", x)
x *= b
print("x *= b:", x)
x /= b
print("x /= b:", x)
x //= b
print("x //= b:", x)
x %= b
print("x %= b:", x)
x **= b
print("x **= b:", x)
print("\n=== Bitwise Operators ===")
print("a & b =", a & b)   # AND
print("a | b =", a | b)   # OR
print("a ^ b =", a ^ b)   # XOR
print("~a =", ~a)         # NOT
print("a << 2 =", a << 2) # Left shift
print("a >> 2 =", a >> 2) # Right shift
print("\n=== Membership Operators ===")
my_list = [1, 2, 3, 10, 20]
print("a in my_list:", a in my_list)
print("b not in my_list:", b not in my_list)
print("\n=== Identity Operators ===")
c = a
print("a is c:", a is c)
print("a is not b:", a is not b)