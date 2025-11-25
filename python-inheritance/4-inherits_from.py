#!/usr/bin/python3
""" Tired of writing comments """


def inherits_from(obj, a_class):
    """ This time also """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
