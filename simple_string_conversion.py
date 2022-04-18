str = 'abc'
from string import ascii_lowercase


def string_conversion(str):
    empty = ''
    for c in str:
        if c in ascii_lowercase:
            empty = empty + ascii_lowercase[str.index(c)+1]
    print(empty)

string_conversion(str)
