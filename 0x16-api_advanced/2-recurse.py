#!/usr/bin/python3
'''
A scripts that returns a list containing the titles of all hot
articles for a given subreddit
'''
import requests


def recurse(subreddit, hot_list=[], count=0, after=''):
    ''' subreddit hot list '''
    url = 'https://www.reddit.com/r/' + subreddit + '/hot/.json'
    resp = requests.get(url, headers={'User-Agent': 'dive'},
                        params={'after': after,
                                'count': count})
    if resp.status_code == 404:
        return None
    resp = resp.json()
    res = resp.get('data').get('children')
    for x in res:
        hot_list.append(x.get('data').get('title'))
    after = resp.get('data').get('after')
    count += resp.get('data').get('dist')
    if after:
        return recurse(subreddit, hot_list, count, after)
    return hot_list
