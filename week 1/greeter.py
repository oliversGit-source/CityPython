def greet_user(name):
    '''Display a simple greeting.'''
    print(f'Greetings, {name}')


def formatted_name(firstName, lastName):
    '''Greet user by full name, neatly formatted'''
    fullName = f'{firstName} {lastName}!'
    return fullName


def main():
    name = input('What is your name?').split()
    greet_user(' '.join(name))
    name2 = formatted_name(name[0], name[1])
    print(f'Hello {name2}!')
    print(f'Farewell {name2}! You are a Git master now!')

main()