#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {res.status_code}")
    if res.status_code == 200:
        res_json = res.json()
        for i in res_json:
            print(i["title"])

def fetch_and_save_posts():
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = []
    if res.status_code == 200:
        for i in res.json():
            post = {}
            post["id"] = i["id"]
            post["title"] = i["title"]
            post["body"] = i["body"]
            posts.append(post)
        with open('posts.csv', "w") as p:
            writer = csv.DictWriter(p, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
