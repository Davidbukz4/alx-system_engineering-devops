#!/usr/bin/python3
'''
A scripts that returns the number of subscribers for a given subreddit
'''
import requests


def number_of_subscribers(subreddit):
    ''' subreddit subscriber '''
    url = 'https://reddit.com/r/' + subreddit + '/about/.json'
    resp = requests.get(url, headers={'User-Agent': 'dive'},
                        allow_redirects=False).json()
    return resp.get('data', {}).get('subscribers', 0)
