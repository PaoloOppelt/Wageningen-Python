from string_splitting import str_splice


num_1 = input("Enter lat1 number e.g. '+1 30 40' for city 1:")
num_2 = input("Enter lon1 number e.g. '+1 30 40' for city 1:")
num_3 = input("Enter lat2 number e.g. '+1 30 40' for city 2:")
num_4 = input("Enter lon2 number e.g. '+1 30 40' for city 2:")


lat_sgn_1, lat_deg_1, lat_min_1 = str_splice(num_1)
lon_sgn_1, lon_deg_1, lon_min_1 = str_splice(num_2)
lat_sgn_2, lat_deg_2, lat_min_2 = str_splice(num_3)
lon_sgn_2, lon_deg_2, lon_min_2 = str_splice(num_4)


lat_sgn_1 = int(lat_sgn_1)
lat_deg_1 = int(lat_deg_1)
lat_min_1 = int(lat_min_1)
lon_sgn_1 = int(lon_sgn_1)
lon_deg_1 = int(lon_deg_1)
lon_min_1 = int(lon_min_1)
lat_sgn_2 = int(lat_sgn_2)
lat_deg_2 = int(lat_deg_2)
lat_min_2 = int(lat_min_2)
lon_sgn_2 = int(lon_sgn_2)
lon_deg_2 = int(lon_deg_2)
lon_min_2 = int(lon_min_2)

from flying_distances_1 import distance

# print(lat_sgn_1, lat_deg_1, lat_min_1,
#         lon_sgn_1, lon_deg_1, lon_min_1,
#         lat_sgn_2, lat_deg_2, lat_min_2,
#         lon_sgn_2, lon_deg_2, lon_min_2)
distance(lat_sgn_1, lat_deg_1, lat_min_1,
        lon_sgn_1, lon_deg_1, lon_min_1,
        lat_sgn_2, lat_deg_2, lat_min_2,
        lon_sgn_2, lon_deg_2, lon_min_2)

# works correctly!
# correct: input for not natural_ sign, degrees, min; Amsterdam to Montreal
# lat Amst/lat1: 1 52 22
# lon Amst/lon1: 1 4 32
# lat Mont/lat2: 1 45 30
# lon Mont/lon2: -1 73 35
# upper value order in comma delimited form: 1, 52, 22, 1, 4, 32, 1, 45, 30, -1, 73, 35
# correct: natural input; Amsterdam to Montreal
# # 52 22 N; 4 32 E; 45 30 N; 73 35 W