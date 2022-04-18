import math


# r = radius h = height
# ca = area of one of the circles
# v = volume
# sa = surface area (the entire outside 'skin' of the cylinder)

def cylinder(r, h):
    ca = math.pi * r ** 2
    print('area:', ca)
    v = ca * h
    print('volume:', v)
    area_sides = 2 * math.pi * r * h
    sa = 2 * ca + area_sides
    print('surface area', sa)


print(cylinder(2, 5))
