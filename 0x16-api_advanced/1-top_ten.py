#!/usr/bin/python3
'''
A scripts that returns the first 10 hot posts listed for a given subreddit
'''
import requests


def top_ten(subreddit):
    ''' subreddit top ten posts '''
    url = 'https://www.reddit.com/r/' + subreddit + '/hot/.json'
    resp = requests.get(url, headers={'User-Agent': 'dive'},
                        params={'limit': 10})
    if resp.status_code == 404:
        print('None')
        return
    resp = resp.json()
    res = resp.get('data').get('children')
    for x in res:
        print(x.get('data').get('title'))
