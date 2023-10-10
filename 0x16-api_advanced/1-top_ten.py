#!/usr/bin/python3
"""
Module: reddit_top_ten

This module contains a function to fetch and print the titles of the first 10
hot posts for a given subreddit using the Reddit API.
"""

import json
import requests
import sys

headers = {
    'User-Agent': 'My User Agent 1.0'
}


def top_ten(subreddit):
    """function that returns the titles of the first 10 hot posts"""
    try:
        url = 'https://www.reddit.com/r/'
        response = requests.get(url + subreddit + "/hot.json?limit=10",
                                headers=headers, allow_redirects=False)
        myArray = [element['data']['title'] for element in response.
                   json()['data']['children']]
        print(*myArray, sep='\n')
    except:
        print(None)
