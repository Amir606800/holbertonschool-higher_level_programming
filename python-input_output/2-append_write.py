#!/usr/bin/python3
"""
    we will give permission to
    write the file and write something in it
"""


def append_write(filename="", text=""):
    """ Open the file with the write write mode """

    with open(filename, "a") as f:
        return f.write(text)
