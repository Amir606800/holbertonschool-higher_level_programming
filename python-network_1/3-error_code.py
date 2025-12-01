#!/usr/bin/python3
""" Error codes handling """
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import sys


url = sys.argv[1]
headers = {'cfclearance': 'true'}
req = Request(url, headers = headers)

try:
    with urlopen(req) as res:
        print(res.read().decode())
except HTTPError as e:
    print(f"Error code: {e}")
