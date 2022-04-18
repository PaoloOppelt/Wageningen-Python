# how could I prompt the user for all values for the function?

def limit(a, b, c):
    if b <= a <= c:
        return a
    elif a < b:
        return b
    else:
        return c


print(limit(-5, 0, 2))
