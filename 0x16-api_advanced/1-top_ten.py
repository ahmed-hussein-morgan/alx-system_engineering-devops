#!/usr/bin/python3
"""The ability to print popular posts certain Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the top ten posts' titles from a particular subreddit."""
    lin = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    params = {
        "limit": 10
    }
    response = requests.get(lin, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
