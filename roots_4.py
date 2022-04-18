import math


def roots(a, b, c):
    discr = (b ** 2 - 4 * a * c)
    if discr >= 0:
        x_1 = (-b + math.sqrt(discr)) / (2 * a)
        x_2 = (-b - math.sqrt(discr)) / (2 * a)
        list = []
        list.append(x_1)
        list.append(x_2)
        return list
        # print(x_1, x_2)


input = input('Enter three values:')
a, b, c = input.split(' ')
a = float(a)
b = float(b)
c = float(c)
# -2, -5, -2 --> -2 -0.5

print(roots(a, b, c))