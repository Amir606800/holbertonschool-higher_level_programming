#!/usr/bin/python3
"""
    we will give permission to
    write the file and write something in it
"""


def write_file(filename="", text=""):
    """ Open the file with the write write mode """

    with open(filename, "w") as f:
        f.write(text)
