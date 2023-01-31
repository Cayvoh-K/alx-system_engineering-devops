#!/usr/bin/python3
"""Function that prints hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        r = r.json()
        for i in range(10):
            print(r['data']['children'][i]['data']['title'])
    else:
        print(None)
