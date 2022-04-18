str = '-1 50'


def str_splice(str):
    # finding the first occurrence
    in_1 = str.index(' ')
    # finding the last occurrence
    in_2 = str.rindex(' ')
    # print(in_1, in_2)
    # using string slice to create substrings
    str_1 = (str[:in_1])
    str_2 = str[in_1 + 1:in_2]
    str_3 = str[in_2 + 1:]

    return str_1, str_2, str_3
    # print(str[:in_1])
    # print(str[in_1 + 1:in_2])
    # print(str[in_2 + 1:])

    # arr = [str[:in_1], str[in_1 + 1:in_2], str[in_2 + 1:]]
    # print(arr)


# print(str_splice(str))
(str_splice(str))
