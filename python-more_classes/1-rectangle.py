#!/usr/bin/python3
""" We will Create an empty Rectangle class"""


class Rectangle:
    """ Here we will pass the methods in order to create an empty class"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """ Setting and Getting the variables """
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError
        self.__height = value
