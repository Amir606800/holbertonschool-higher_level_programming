#!/usr/bin/python3
""" Request id with request """
import requests
import sys


if len(sys.argv) >= 2:
    req = requests.get(sys.argv[1])
    print(req.headers["X-Request-Id"])
else:
    print()
