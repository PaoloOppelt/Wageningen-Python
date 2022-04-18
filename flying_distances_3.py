from string_splitting import str_splice

input_1_str = input("Enter lat1 number e.g. '30° 40' N' for city 1:")
input_2_str = input("Enter lon1 number e.g. '52° 0' E' for city 1:")
input_3_str = input("Enter lat2 number e.g. '30° 40' N' for city 2:")
input_4_str = input("Enter lon2 number e.g. '52° E' for city 2:")


def convert_natural(input):
    degrees, min, hemisphere = str_splice(input)
    if not degrees.isalnum():
        degrees = degrees[:-1]
    if not min.isalnum():
        min = min[:-1]
    if min == '':
        min = 0
    if hemisphere == 'N':
        hemisphere = 1
    if hemisphere == 'E':
        hemisphere = 1
    else:
        hemisphere = -1
    # switching order; min stay the same
    sgn = hemisphere
    deg = int(degrees)
    min = int(min)
    # print(type(sgn), type(deg), type(min))
    return sgn, deg, min


lat_sgn_1, lat_deg_1, lat_min_1 = convert_natural(input_1_str)
lon_sgn_1, lon_deg_1, lon_min_1 = convert_natural(input_2_str)
lat_sgn_2, lat_deg_2, lat_min_2 = convert_natural(input_3_str)
lon_sgn_2, lon_deg_2, lon_min_2 = convert_natural(input_4_str)

# print(lat_sgn_1, lat_deg_1, lat_min_1, lon_sgn_1, lon_deg_1, lon_min_1, lat_sgn_2, lat_deg_2, lat_min_2, lon_sgn_2, lon_deg_2, lon_min_2)

from flying_distances_1 import distance

distance(lat_sgn_1, lat_deg_1, lat_min_1,
        lon_sgn_1, lon_deg_1, lon_min_1,
        lat_sgn_2, lat_deg_2, lat_min_2,
        lon_sgn_2, lon_deg_2, lon_min_2)

# correct: input for not natural_ sign, degrees, min; Amsterdam to Montreal
# lat Amst/lat1: 1 52 22
# lon Amst/lon1: 1 4 32
# lat Mont/lat2: 1 45 30
# lon Mont/lon2: -1 73 35
# upper value order in comma delimited form: 1, 52, 22, 1, 4, 32, 1, 45, 30, -1, 73, 35
# correct: natural input; Amsterdam to Montreal
# # 52 22 N; 4 32 E; 45 30 N; 73 35 W