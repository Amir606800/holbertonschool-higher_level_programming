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
            pickle.dump(self, f)
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
