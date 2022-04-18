# n = int(input('Input a number:'))
input_str = input('Input a list of numbers separated by comma:')

l = input_str.split(',')
def sum_odd(l):
    total = 0
    # range fist input is from and second means until
    # don't call a list 'list'
    l = list(map(int, l))
    for i in l:
        if not (i % 2) == 0:
            total = total + i
    return total


print(sum_odd(l))
