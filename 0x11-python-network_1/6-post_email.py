#!/usr/bin/python3
"""Python script that takes in a URL and an email address"""
from requests import post
from sys import argv


if __name__ == "__main__":
    email = {'email': argv[2]}
    res = post(argv[1], data=email)
    print(res.text)
