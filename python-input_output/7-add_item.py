#!/usr/bin/python3
""" Frist import the necessary modules """
import json  # To use the json formatting in our code
import sys  # In order to get the arguments from the command
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

all_args = sys.argv[1:]
if load_from_json_file("add_item.json"):
    prev_list = load_from_json_file("add_item.json")
    all_args = all_args.extend(prev_list)
save_to_json_file(all_args, "add_item.json")
