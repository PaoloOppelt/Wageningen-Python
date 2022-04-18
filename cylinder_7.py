import math
from string_splitting import str_splice

# r = radius h = height
# ca = area of one of the circles
# v = volume
# sa = surface area (the entire outside 'skin' of the cylinder)


def area_and_volume(r, h):
    ca = math.pi * r ** 2
    volume = ca * h
    area_sides = 2 * math.pi * r * h
    area = 2 * ca + area_sides
    return volume, area


str = input('input radius and height:')
# n represents the middle value which is nothing in this case because the input are only two numbers not 3
r, n, h = str_splice(str)
r = float(r)
h = float(h)
print(r, h)
print(area_and_volume(r, h))


# while r or h != 'break':
#     r = input('input radius:')
#     if r == 'break':
#         break
#     r = float(r)
#     h = input('input height:')
#     if h == 'break':
#         break
#     h = float(h)
#     print(area_and_volume(r, h))
#
# r = ''
# h = ''
# while r or h != 'break':
#     r = input('input radius:')
#     if r == 'break':
#         break
#     r = float(r)
#     h = input('input height:')
#     if h == 'break':
#         break
#     h = float(h)
#     print(area_and_volume(r, h))


# print(area_and_volume(2, 5))
