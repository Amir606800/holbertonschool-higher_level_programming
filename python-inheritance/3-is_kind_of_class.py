#!/usr/bin/python3
""" creating the checker part 2 """


def is_kind_of_class(obj, a_class):
    """ Checking the type and the subclass of tthe objects """

    if type(obj) is a_class or issubclass(obj, a_class):
        return True
    return False
