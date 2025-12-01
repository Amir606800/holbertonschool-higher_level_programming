#!/usr/bin/python3
""" Requesting form from intranet holberton """
from urllib.request import Request, urlopen

headers = {'cfclearance': 'true'}
req = Request("https://intranet.hbtn.io/status")
with urlopen(req) as web:
    reset = web.read()
    print("Body response:")
    print(f"\t- type: {type(reset)}")
    print(f"\t- content: {reset}")
    print(f"\t- utf8 content: {reset.decode('utf-8')}")
