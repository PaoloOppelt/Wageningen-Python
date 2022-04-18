from string_splitting import str_splice

def convert_natural(input):
    degrees, min, hemisphere = str_splice(input)
    print(degrees, min, hemisphere)
    if not degrees.isalnum():
        degrees = degrees[:-1]
    if not min.isalnum():
        min = min[:-1]
    if min == '':
        min = 0
# why is this function not working. How am I supposed to use or?
    if hemisphere == 'N' or 'E':
        hemisphere = 1
    else:
        hemisphere = -1
    # switching order; min stay the same
    sgn = hemisphere
    deg = int(degrees)
    min = int(min)
    # print(type(sgn), type(deg), type(min))
    return sgn, deg, min

input_1_str = '73 35 W'

print(convert_natural(input_1_str))

# correct: input for not natural_ sign, degrees, min; Amsterdam to Montreal
# lat Amst/lat1: 1 52 22
# lon Amst/lon1: 1 4 32
# lat Mont/lat2: 1 45 30
# lon Mont/lon2: -1 73 35
# upper value order in comma delimited form: 1, 52, 22, 1, 4, 32, 1, 45, 30, -1, 73, 35
# correct: natural input; Amsterdam to Montreal
# # 52 22 N; 4 32 E; 45 30 N; 73 35 W