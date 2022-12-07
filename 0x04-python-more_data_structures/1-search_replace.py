#!/usr/bin/python3
def search_replace(my_list, search, replace):
    length = len(my_list)
    new_list = []
    if length > 0:
        for num in my_list:
            if num == search:
                new_list.append(replace)
            else:
                new_list.append(num)
    return new_list
