#!/usr/bin/python3
"""Python script that takes GitHub credentials"""

from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ = "__main__":
    url = 'https://api.github.com/user'
    res = get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    try:
        obj = res.json()
        print(obj.get('id'))
    except ValueError:
        print(None)
