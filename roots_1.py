import math

a = -2
b = -5
c = -2
discr = (b**2-4*a*c)


if discr >= 0:
    x_1 = (-b + math.sqrt(discr)) / (2 * a)
    x_2 = (-b - math.sqrt(discr)) / (2 * a)
    print(x_1, x_2)