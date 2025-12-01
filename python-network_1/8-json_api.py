#!/usr/bin/python3
""" Searching in a website via python """
import sys
import requests


if len(sys.argv) >= 2:
    q = sys.argv[1]
else:
    q = ""

response = requests.post(f"http://0.0.0.0:5000/search_user?q={q}")
res_json = response.json()
if len(res_json) > 0:
    print(res_json)
elif res_json == 0:
    print("No result")
else:
    print("Not a valid JSON")
