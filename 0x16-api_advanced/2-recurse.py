#!/usr/bin/python3
"""
function that queries the reddit API and prints
the top ten hot posts of a subreddit
"""
import requests
import sys

def add_title(hot_list, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)

def recurse(subreddit, after=None, hot_list=[]):
    headers = {'User-Agent': 'MyBot/1.0'}
    params = {'limit': 100, 'after': after}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        hot_posts = data['data']['children']
        after = data['data']['after']
        
        for post in hot_posts:
            hot_list.append(post['data']['title'])
        
        if after:
            return recurse(subreddit, after, hot_list)
        else:
            return hot_list
    else:
        return None

