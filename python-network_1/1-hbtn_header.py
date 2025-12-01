#!/usr/bin/python3
""" Comment """
from urllib.request import Request, urlopen
import sys


if len(sys.argv) >= 2:
    argument = sys.argv[1]
    req = argument
    with urlopen(req) as web:
        print(web.headers["X-Request-Id"])
else:
    print()
