#!/usr/bin/python3
"""Task-2"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Task-2"""
    u = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after)
    r = requests.get(u, headers={'User-agent': 'r'}, allow_redirects=False)
    if r.status_code == 200:
        r = r.json()
        for x in r.get('data').get('children'):
            hot_list.append(x.get('data').get('title'))
        id = r.get('data').get('after')
        if id is not None:
            recurse(subreddit, hot_list, id)
        return hot_list
    else:
        return None
