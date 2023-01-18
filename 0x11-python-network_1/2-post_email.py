#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""ython script that takes in a URL and an email, sends a POST request"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == '__main__':
    email = {'email': argv[2]}
    email = urlencode(email)
    email = email.encode('ascii')
    request = Request(argv[1], email)
    with urlopen(request) as response:
        string = response.read().decode('utf-8')
        print(string)
