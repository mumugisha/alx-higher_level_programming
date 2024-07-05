#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
Handles HTTPError and URLError exceptions.
"""

import sys
from urllib import request, error

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        req = request.Request(url)
        with request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("HTTP Error code: {}".format(err.code))
    except error.URLError as err:
        if hasattr(err, 'reason'):
            print("URL Error: {}".format(err.reason))
        elif hasattr(err, 'code'):
            print("HTTP Error code: {}".format(err.code))
