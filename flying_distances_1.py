from math import sin, sqrt, cos, atan2, radians, pi
import math


def converting_rad(sign, deg, min):
    all_deg = deg + min / 60
    rad = all_deg * math.pi / 180
    rad = sign * rad
    return rad


def haversine(lat1, lat2, lon1, lon2):
    # converting (lat1, lon1, lat2, lon2)
    r = 1
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a_sq = (sin(dlat / 2)) ** 2 + cos(lat1) * cos(lat2) * (sin(dlon / 2)) ** 2
    b_sq = r - a_sq
    d = 2 * atan2(sqrt(a_sq), sqrt(b_sq))
    kilometers = d * 6367
    print(kilometers)


def distance(lat_sgn_1, lat_deg_1, lat_min_1,
             lon_sgn_1, lon_deg_1, lon_min_1,
             lat_sgn_2, lat_deg_2, lat_min_2,
             lon_sgn_2, lon_deg_2, lon_min_2):
    lat1 = converting_rad(lat_sgn_1, lat_deg_1, lat_min_1)
    lon1 = converting_rad(lon_sgn_1, lon_deg_1, lon_min_1)
    lat2 = converting_rad(lat_sgn_2, lat_deg_2, lat_min_2)
    lon2 = converting_rad(lon_sgn_2, lon_deg_2, lon_min_2)
    haversine(lat1, lat2, lon1, lon2)

# works correctly!

# correct: input for not natural_ sign, degrees, min; Amsterdam to Montreal
# lat Amst/lat1: 1 52 22
# lon Amst/lon1: 1 4 32
# lat Mont/lat2: 1 45 30
# lon Mont/lon2: -1 73 35
# upper value order in comma delimited form: 1, 52, 22, 1, 4, 32, 1, 45, 30, -1, 73, 35
# correct: natural input; Amsterdam to Montreal
# # 52 22 N; 4 32 E; 45 30 N; 73 35 W
