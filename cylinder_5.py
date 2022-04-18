import math


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


print(area_and_volume(2, 5))
