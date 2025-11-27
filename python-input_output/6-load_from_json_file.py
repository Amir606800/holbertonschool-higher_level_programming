#!/usr/bin/python3
""" We will use the json library and open it with open() """
import json


def load_from_json_file(filename):
    """
      Here we will use json.load in order to parse
      the json format into the string format
    """

    with open(filename) as f:
        return json.load(f)
