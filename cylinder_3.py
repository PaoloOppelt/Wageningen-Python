import math


# r = radius h = height
# ca = area of one of the circles
# v = volume
# sa = surface area (the entire outside 'skin' of the cylinder)

def cylinder(r):
    ca = math.pi * r ** 2
    return ca


def volume(r, h):
    ca = math.pi * r ** 2
    v = ca * h
    # print('volume:', v)
    return v


def surface_area(r, h):
    area_sides = 2 * math.pi * r * h
    ca = math.pi * r ** 2
    sa = 2 * ca + area_sides
    return sa


print(volume(2, 5), surface_area(2, 5))
