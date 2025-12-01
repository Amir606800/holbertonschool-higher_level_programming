#!/usr/bin/python3
""" Searching in a website via python """
import sys
import requests


if len(sys.argv) >= 2:
    q = sys.argv[1]
else:
    q = ""

try:
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q}, headers={'cfclearance': 'true'})
    res_json = response.json()
except ValueError:
    print("Not a valid JSON")

if res_json:
    print(f"[{res_json.get('id')}] {res_json.get('name')}")
else:
    print("No result")
