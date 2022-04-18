def inprod():
    l_1 = [3, -2, 0, 1]
    l_2 = [3, 4, 2, -5]
    if len(l_1) == len(l_2):
        sum = 0
        for i in range(len(l_1)):
            product = l_1[i] * l_2[i]
            sum += product
        return sum
print(inprod())



# when done use the try and except functions