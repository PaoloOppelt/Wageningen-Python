import math

def roots(a, b, c):
    discr = (b ** 2 - 4 * a * c)
    if discr >= 0:
        x_1 = (-b + math.sqrt(discr)) / (2 * a)
        x_2 = (-b - math.sqrt(discr)) / (2 * a)
        return x_1, x_2
        #print(x_1, x_2)

roots(-2, -5, -2)