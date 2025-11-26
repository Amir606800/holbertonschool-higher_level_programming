#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry
""" Creating the second class which inherits from first one """


class Rectangle(BaseGeometry):
    """ Now we instantinate the class """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
