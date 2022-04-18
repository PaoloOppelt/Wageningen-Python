# use the split function to directly insert the words in a string into a list
str_list = list(input('Insert a string of words separated by spaces:').split())
pattern_str = input('Insert a pattern:')

def count_pattern():
    pattern_list = []
    pattern_list.append(pattern_str)

    count = 0
    # error resolved: use i in range(length or list) not i in str_list
    for i in range(len(str_list)):
        if pattern_list[0] in str_list[i]:
            count += 1
        return count

print(count_pattern())