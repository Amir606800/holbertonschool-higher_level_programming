#!/usr/bin/python3
"""
  Importing A CSV data into
  Python and Printing JSON Format
"""
import json
import csv


def convert_csv_to_json(filename):
    """
    Burda ilk once file-i csv den dictionary
    sekline cevirmeye
    calisiriq daha sonra ise
    onu list edib json ile dump edirik yeni file-a
    """
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open("data.json", "w") as f:
            json.dump(data, f)
        return True
    except FileNotFoundError:
        return False
