'''
word = input("Write a WORD HERE.")

def doTwice(word):
    print("2nd run.")
    return word

@doTwice

def sayWord(word):
    print("1st run.")
    return word

sayWord(word)
'''

def doTwice(function):
    def twoCalls(somePara):
        function(somePara)
        function(somePara)
    return twoCalls

@doTwice
def sayWord(word):
    print(word)

if __name__ == "__main__":
    word = input('Enter a word:')
    sayWord(word)