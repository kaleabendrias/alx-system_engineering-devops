#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data')
    children = data.get('children')

    for i in range(10):
        print(children[i].get('data').get('title'))
