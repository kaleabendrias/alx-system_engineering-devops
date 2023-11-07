#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles"""
    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        for post in data['data']['children'][:10]:
            print(post['data']['title'])
    except Exception:
        print(None)