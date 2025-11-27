#!/usr/bin/python3
""" Frist import the necessary modules """
import sys  # In order to get the arguments from the command
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

all_args = sys.argv[1:]
try:
    """ Try if the list is aviable then load """
    prev_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    """ If not then create an empty list """
    prev_list = []
"""
  At the end we will just
  extend the list and save
  the new args into it
"""
prev_list.extend(all_args)
save_to_json_file(prev_list, "add_item.json")
