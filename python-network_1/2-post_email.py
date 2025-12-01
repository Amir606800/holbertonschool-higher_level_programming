#!/usr/bin/python3
""" POSTIng insta post """
from urllib.request import Request, urlopen
import urllib.parse
import sys


def post_insta():
    if len(sys.argv) < 3:
        return
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')
    headers = {'cfclearance': 'true'}
    req = Request(url, data = data, headers = headers)
    with urlopen(req) as r:
        print(r.read().decode())

post_insta()
