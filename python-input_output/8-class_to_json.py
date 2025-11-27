#!/usr/bin/python3
""" First create the function """


def class_to_json(obj):
    """ The just dump the object's dictionary """
    return obj.__dict__
