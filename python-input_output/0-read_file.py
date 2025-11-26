#!/usr/bin/python3
""" Writing the function for the file to be open """


def read_file(filename=""):
    """
       We specified the filename and open it with
       "with" statement and the "open" object.
       "with" will handle the closing of the file.
    """

    with open(filename) as f:
        print(f.read())
