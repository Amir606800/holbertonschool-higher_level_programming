#!/usr/bin/python3
""" Creating the inherited MyList class """


class MyList(list):
    """ First we will create the print_sorted method """

    def print_sorted(self):
        new_list = self + []
        new_list.sort()
        print(new_list)
