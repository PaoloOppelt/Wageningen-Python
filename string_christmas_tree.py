star = '*'
space = ' '
bar = '|'

# 15 characters per line
# s stands for space
# str stands for star
# r stands for range


def christmas_tree(r):
    s = 6
    str = 1
    for i in range(r):
        print(bar + space * s + star * str + space * s + bar)
        s = s - 1
        str = str + 2
    print(space*7+bar+space*7)

# change r value depending on the desired height of the tree
print(christmas_tree(3))


# print(bar + space * 6 + star + space * 6 + bar)
# print(bar + space * 5 + star * 3 + space * 5 + bar)
# print(bar + space * 5 + star * 3 + space * 5 + bar)
