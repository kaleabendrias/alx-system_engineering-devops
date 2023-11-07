#!/usr/bin/python3
"""function that queries the Reddit API and returns a list containing the"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """function that queries the Reddit API and returns a list containing"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    children = data.get('children')
    after = data.get('after')

    for child in children:
        hot_list.append(child.get('data').get('title'))

    if after is not None:
        recurse(subreddit, hot_list, after)

    return hot_list
