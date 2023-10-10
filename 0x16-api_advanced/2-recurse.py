#!/usr/bin/python3
"""
Module: reddit_recursive

This module contains a recursive function to fetch the titles of all hot
articles for a given subreddit using the Reddit API.
"""

import json
import requests
import sys

headers = {
    'User-Agent': 'My User Agent 1.0'
}
after = None


def recurse(subreddit, hot_list=[]):
    """function that returns a list with the titles of all hot articles"""
    try:
        url = 'https://www.reddit.com/r/'
        global after
        if after:
            response = requests.get(url + subreddit + "/hot.json?after=" +
                                    after, headers=headers,
                                    allow_redirects=False)
        else:
            response = requests.get(url + subreddit + "/hot.json",
                                    headers=headers, allow_redirects=False)
        after = response.json()['data']['after']
        hot_list += [element['data']['title'] for element in response.
                     json()['data']['children']]
        if after:
            return recurse(subreddit, hot_list)
        return hot_list
    except:
        return None
