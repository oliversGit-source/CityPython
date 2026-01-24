name = list(input("Write your name here to check if this is a palindrome:"))
if name[::-1] == name[::1]:
    print("This name is a palindrome.")
else:
    print("This name is not a palindrome.")