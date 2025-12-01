#!/usr/bin/python3
""" New method: Using requests """
import requests


r = requests.get("https://intranet.hbtn.io/status")
print("Body response:")
print(f"\t- type: {type(r)}")
print(f"\t- content: {r.text}")
