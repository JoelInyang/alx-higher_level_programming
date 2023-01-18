#!/usr/bin/python3
"""Python script that takes in a URL"""

from requests import get
from sys import argv

if __name__ == "__main__":
    response = get(argv[1])
    i = response.headers
    print(i.get("X-Request-Id"))
