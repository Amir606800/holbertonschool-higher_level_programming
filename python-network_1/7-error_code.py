#!/usr/bin/python3
""" Error handling """
import requests
import requests.exceptions as re
import sys


if len(sys.argv) < 2:
    print()
else:
    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
