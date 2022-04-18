M = [[13, -2, 5], [0, 100, 9], [-13, 27, -10]]


def sum_matrix_elements():
    sum = 0
    for rows in M:
        for elements in rows:
            sum += elements
    print(sum)


# printing matrix not working:
# str_matrix = ''
# for row in M:
#     for element in row:
#         str_matrix = str_matrix+str(element)+'/t'
# print(str_matrix)


# creates a matrix by rows = n; columns = m of only zeros that are not aliasing in each row.
# Aliasing is what would happen by default with this formula:
# L = [[0]*5]*5 (for a 5*5 matrix)


def zero_matrix(c, r):
    total = []
    for i in range(r):
        total += [[0] * c]
    return total


matrix = zero_matrix(3, 3)
matrix[0][0] = 1
