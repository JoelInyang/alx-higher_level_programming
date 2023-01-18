#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Python script that takes in, sends, display a url"""
import urllib.request
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    with urllib.request.urlopen(url) as res:
        info = res.info()
        print(info['X-Request-Id'])
