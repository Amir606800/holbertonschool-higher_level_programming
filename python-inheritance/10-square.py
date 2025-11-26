#!/usr/bin/python3
""" The first thing is import the Rectangle class to this code """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Now let's init the class """

    def __init__(self, size):
        super().__init__(size, size)
