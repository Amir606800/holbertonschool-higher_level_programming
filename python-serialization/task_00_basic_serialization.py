#!/usr/bin/pyhton3
""" Serialization and deserialization """
import json


def serialize_and_save_to_file(data, filename):
    """
      Serialization with dump
      because we have data
      and the destination file
    """
    with open(filename, "w") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    with open(filename, "r") as f:
        return json.loads(f)

