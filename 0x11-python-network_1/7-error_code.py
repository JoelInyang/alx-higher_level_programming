#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""
from requests import get
from sys import argv


if __name__ == "__main__":
    res = get(argv[1])
    if res.status_code < 400:
        print(res.text)
    else:
        print('Error code: {}'.format(res.status_code))
