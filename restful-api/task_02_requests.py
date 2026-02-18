#!/usr/bin/python3

import requests
import json
import csv

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        print("Status Code: {}".format(r.status_code))
        data = r.json()

        for i in data:
            print(i['title'])
    else:
        print(r.status_code)

import requests
import csv

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if r.status_code == 200:
        print("Status Code: {}".format(r.status_code))
        posts = r.json()

        structured_posts = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_posts)
        
    else:
        print("Status Code: {}".format(r.status_code))

