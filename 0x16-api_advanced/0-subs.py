#!/usr/bin/python3
"""
function that queries the reddit API and returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'MyBot/1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
