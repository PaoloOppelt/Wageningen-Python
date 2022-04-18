# use the split function to directly insert the words in a string into a list
substring = 'he'
string = 'hello world hello'

def count_pattern(substring, string):
    pattern_list = []
    pattern_list.append(substring)
    str_list = list(string.split())
    count = 0
    for i in range(len(str_list)):
        if pattern_list[0] in str_list[i]:
            count += 1
        return count


# print(count_pattern(substring, string))

def remove_substring_occurrence_1(substring, string):
    pattern_list = []
    pattern_list.append(substring)
    str_list = list(string.split())
    for i in range(len(str_list)):
        if pattern_list[0] in str_list[i]:
            str_list[i] = str_list[i].replace(pattern_list[0], '')
            break
    return str_list


# print(remove_substring_occurrence_1(substring, string))


def remove_substring(substring, string):
    pattern_list = []
    pattern_list.append(substring)
    str_list = list(string.split())
    for i in range(len(str_list)):
        if pattern_list[0] in str_list[i]:
            str_list[i] = str_list[i].replace(pattern_list[0], '')
    return str_list


# print(remove_substring(substring, string))
