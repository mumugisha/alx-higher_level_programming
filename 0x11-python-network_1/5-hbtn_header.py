#!/usr/bin/python3
'''script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header'''
import sys
from requests import get


if __name__ == '__main__':
    try:
        req = get(sys.argv[1])
        print(req.headers['X-Request-Id'])
    except Exception:
        pass
