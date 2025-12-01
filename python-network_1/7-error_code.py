#!/usr/bin/python3
""" Error handling """
import requests
import requests.exceptions as re
import sys


if len(sys.argv) < 2:
    print()
else:
    url = sys.argv[1]
    try:
        res = requests.get(url)
        print(res.text)
    except re.HTTPError as errh:
        print(f"Error code: {errh.status_ode}")
