#!/usr/bin/python3
"""
Module: reddit_word_counter

This module contains a function to fetch the top posts of a subreddit
and count the occurrences of specified keywords in their titles.
"""

import requests

def count_words(subreddit, keywords, after=None, word_counts=None):
    """
    Recursively fetches top posts of a subreddit and counts occurrences of
    keywords in their titles.
    """
    headers = {
        "User-Agent": "MyBot/1.0"
    }

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"

    if word_counts is None:
        word_counts = {keyword.lower(): 0 for keyword in keywords}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {}).get("children", [])

    for post in data:
        title = post.get("data", {}).get("title", "").lower()
        for keyword in keywords:
            if f" {keyword.lower()} " in f" {title} ":
                word_counts[keyword.lower()] += 1

    next_after = response.json().get("data", {}).get("after")
    if next_after:
        count_words(subreddit, keywords, after=next_after, word_counts=word_counts)
    else:
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_counts:
            if count > 0:
                print(f"{word}: {count}")
