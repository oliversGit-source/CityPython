def palindrome():
    name = input("Write your name here to check if this is a palindrome:")
    capsname = name.upper()

    def prettyPrint(capsname, reversed):
        for letter in capsname:
            if reversed == True:
                print(letter[-1])
            else:
                print(letter[1])

    prettyPrint(capsname, True)
    if capsname[::-1] == capsname[::1]:
        print("This name is a palindrome.")
    else:
        print("This name is not a palindrome.")

palindrome()