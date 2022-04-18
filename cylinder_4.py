import math


# r = radius h = height
# ca = area of one of the circles
# v = volume
# sa = surface area (the entire outside 'skin' of the cylinder)

def area_circle(r):
    ca = math.pi * r ** 2
    return ca


def volume(r, h):
    v = area_circle(r) * h
    # print('volume:', v)
    return v


def surface_area(r, h):
    area_sides = 2 * math.pi * r * h
    sa = 2 * area_circle(r) + area_sides
    return sa


# radius, height
print(volume(2, 5), surface_area(2, 5))
