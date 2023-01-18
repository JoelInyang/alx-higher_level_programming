#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)
    b = response.text
    string = 'Body response:\n\t- type: {}\n\t- content: {}'.format(
             type(b), b)
    print(string)
