#!/usr/bin/python3
"""A file to make a query to an endpoint
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    url = "https://api.reddit.com/r/{}/top/.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Python3"}
    response = requests.request("GET", url, headers=headers).json()
    try:
        for i in range(10):
            print(response['data']['children'][i]['data']['title'])
    except Exception:
        print(None)
