#!/usr/bin/python3

"""evaluates candidates applying for a back-end position"""
from requests import get
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    res = get(url)
    try:
        objects = res.json()
        for i, obj in enumerate(objects):
            print('{}: {}'.format(obj.get('sha'),
                                  obj.get('commit').get('author').get('name')))
            if i == 9:
                break
    except ValueError:
        pass
