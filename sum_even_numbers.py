n = int(input('Input a number:'))


def sum_even(n):
    total = 0
    for i in range(1, n + 1):
        if (i % 2) == 0:
            total = total + i
    return total


print(sum_even(n))
