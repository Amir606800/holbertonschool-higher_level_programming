#!/usr/bin/python3
""" A:JKwfv;wdf """
import pickle


class CustomObject:
    """ Hello """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dumps(f)
    
    def display(self):
        for k, v in self.__dict__:
            print(f"{k}: {v}")

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
