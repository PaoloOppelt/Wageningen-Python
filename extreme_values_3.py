# Write a function that finds the smallest and largest element in a list.
import random
input_str = input('Enter values separated by spaces:')

# input_list = list(input_str.replace(' ',''))
# words or character list
wo_ch_list = list(input_str.split())

#print(wo_ch_list)

random.shuffle(wo_ch_list)

print(wo_ch_list)


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


print(small_large(wo_ch_list))


# we can use the argument-unpacking operator i.e. *
# list = [*range(10, 21)]
# print(list)