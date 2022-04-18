def user_input():
    help = '''   
help:/tno secondary input; the program just prints information about available commands and their inputs
lookup:/t secondary input is a name; the (final) program looks up the number for that name (if any)
enter:/t secondary input consists of a name and a phone number; the (final) program registers the number with the name
remove:/t secondary input is a name; the (final) program removes the name (if any) and corresponding number
quit:/t no secondary input; the program ends'''
    in_str = input('provide input(command):')
    if in_str == 'lookup':
        # in_sec_str = input('provide secondary input (name):')
        in_sec_str = 'name'
        lookup(in_sec_str)
    elif in_str == 'enter':
        # in_sec_str = input('provide secondary input (name, phone_number):')
        in_sec_tuple = 'name', '0123'
        enter(in_sec_tuple)
    elif in_str == 'remove':
        # in_sec_str = input('provide secondary input (name):')
        in_sec_str = 'name'
        remove(in_sec_str)
    elif in_str == 'quit':
        quit()
    else:
        print(help)

user_input()

name = {}


def lookup(name):
    print('looking for', name)


def enter(name, phone_number):
    print('hello', name, 'at', phone_number)


def remove(name):
    print('so long', name)


def quit():
    print('bye')
    exit()
