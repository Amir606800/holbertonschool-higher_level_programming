#!/usr/bin/python3
def max_integer(my_list=[]):
    uz = len(my_list)
    max_int = my_list[0]
    if uz == 0:
        return None
    else:
        for i in my_list:
            if max_int < i:
                max_int = i
    return max_int
