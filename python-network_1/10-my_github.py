#!/usr/bin/python3
""" Logining in to the Github account """
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print()
    else:
        username = sys.argv[1]
        passwd = sys.argv[2]
        url = "https://api.github.com/user"
        res = requests.get(
                url,
                headers={
                    "Authorization": f"token {passwd}",
                }
            )
        if res.status_code >= 400:
            print("None")
        else:
            print(res.json().get("id"))
