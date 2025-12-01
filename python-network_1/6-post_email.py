#!/usr/bin/python3
""" Posting email with requests """
import requests
import sys


if len(sys.argv) >= 3:
    url = sys.argv[1]
    email = sys.argv[2]
    headers = {'cfclearance': 'true'}
    res = requests.post(url, data={"email": email}, headers=headers)
    print(res.text)
else:
    print()
