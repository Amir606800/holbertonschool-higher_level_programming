#!/usr/bin/python3
""" This code will create a new file contains the json formatted strings """
import json


def save_to_json_file(my_obj, filename):
    """
      We will first convert
      the obj to json and
      then write the file
    """

    formatted_string = json.dumps(my_obj)
    with open(filename, "w") as f:
        f.write(formatted_string)
