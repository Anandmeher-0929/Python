# Python Program to check whether a given alphabet is vowel or not
ch = input("Enter an alphabet: ")
ch = ch.lower()
if ch in ['a', 'e', 'i', 'o', 'u']:
    print(f"{ch} is a vowel.")
else:
    print(f"{ch} is not a vowel.")
