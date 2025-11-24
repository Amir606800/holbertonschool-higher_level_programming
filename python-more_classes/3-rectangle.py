#!/usr/bin/python3
""" We will Create an empty Rectangle class"""


class Rectangle:
    """ Here we will pass the methods in order to create an empty class"""
    def __init__(self, width=0, height=0):

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        drawing = ""
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(self.height):
            print(self.width * "#")
        return ""

    def __repr__(self):
        drawing = ""
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(self.height):
            print(self.width * "#")
        return ""
