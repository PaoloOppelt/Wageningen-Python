
def fibonacci():
    fibonacciSeries = [0, 1]
    # range starting 1 until 5
    for i in range(2, 5):
        next_element = fibonacciSeries[i-1] + fibonacciSeries[i-2]
        fibonacciSeries.append(next_element)
    return fibonacciSeries


print(fibonacci())

# my failed try:
# def fibonacci():
#     fib_0 = 0
#     fib_1 = fib_2 = 1
#     for i in range(5):
#         i[0] =0
#
#         return i
#     return fib_0, fib_1, fib_2
#
#
# print(fibonacci())