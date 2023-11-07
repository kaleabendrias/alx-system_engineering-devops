#!/usr/bin/python3
"""parses the title of all hot articles, and prints a sorted"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None, count_dict={}):
    """parses the title of all hot articles, and prints a sorted"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data')
    children = data.get('children')
    after = data.get('after')

    for child in children:
        hot_list.append(child.get('data').get('title'))

    if after is not None:
        count_words(subreddit, word_list, hot_list, after, count_dict)

    for title in hot_list:
        words = title.lower().split()
        for word in words:
            if word in word_list:
                if word in count_dict:
                    count_dict[word] += 1
                else:
                    count_dict[word] = 1

    sorted_list = sorted(count_dict.items(), key=lambda x: (-x[1], -x[0]))
    last_occurrence = {}
    for key, value in count_dict.items():
        last_occurrence[key] = value
    for key, value in last_occurrence.items():
        print(f"{key}: {value}")
