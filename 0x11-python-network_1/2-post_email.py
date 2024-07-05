#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the
email as a parameter, and displays the body of
the response (decoded in utf-8).
"""
import sys
from urllib import parse, request, error

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: ./script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    
    print(f"URL: {url}")
    print(f"Email: {email}")

    try:
        dataset = parse.urlencode({'email': email})
        req = request.Request(url, data=dataset.encode('ascii'))
        with request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except error.URLError as e:
        print(f"Failed to reach the server: {e.reason}")
    except error.HTTPError as e:
        print(f"Server couldn't fulfill the request. Error code: {e.code}")
    except Exception as e:
        print(f"An error occurred: {e}")
