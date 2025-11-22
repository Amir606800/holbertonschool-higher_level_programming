#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list[:x]:
            print(i, end="")
        return x[-1]
    except TypeError:
        print()
        return my_list[-1]
