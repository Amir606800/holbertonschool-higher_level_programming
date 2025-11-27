#!/usr/bin/python3
""" Create the class Student """


class Student:
    """ Initialize the clas with the given variables """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        di = self.__dict__
        if attrs is None or not isinstance(attrs, list):
            return di
        new_dict = {}
        for i in attrs:
            if i in di:
                new_dict[i] = di[i]
        return new_dict

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
