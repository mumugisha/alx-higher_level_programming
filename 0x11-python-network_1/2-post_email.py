#!/usr/bin/python3
'''script that takes in a URL and an email, sends a POST request,
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
'''
import sys
from urllib import request, parse


if __name__ == '__main__':
    data = parse.urlencode({'email': sys.argv[2]})
    req = request.Request(sys.argv[1], data.encode('ascii'))
    with request.urlopen(req) as res:
        print(res.read().decode('utf8'))

