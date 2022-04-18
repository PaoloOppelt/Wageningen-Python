# Write a function that finds the smallest and largest element in a list.

list = [-1, 2, -100, 30]


def small_large(list):
    n = 0
    smallest = list[0]
    largest = list[0]
    # i for item
    for i in list:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
        n += 1
        index_sm = list.index(smallest)
        index_la = list.index(largest)
    return smallest, index_sm, largest, index_la


print(small_large(list))