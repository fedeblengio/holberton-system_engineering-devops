#!/usr/bin/python3
"""Task-1"""
import requests


def top_ten(subreddit):
    """Api Reddit"""
    u = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    r = requests.get(u, headers={'User-agent': 'r'}, allow_redirects=False)
    if r.status_code == 200:
        d = r.json()
        top = d.get('data').get('children')
        for i in range(10):
            print(top[i].get('data').get('title'))
    else:
        print("None")
        return
