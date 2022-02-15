#!/usr/bin/python3
"""0. How many subs?"""
import requests


def number_of_subscribers(subreddit):
    """redit api"""
    u = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(u, headers={'User-agent': 'Reddit'})
    if r.status_code == 404:
        return 0
    d = r.json()
    sub = d.get('data').get('subscribers')
    return sub
