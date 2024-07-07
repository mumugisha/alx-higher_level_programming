#!/usr/bin/env python3
"""
Python script that takes in a URL and an
email address, sends a POST request to the
passed URL with the email as a parameter,
and finally displays the body of the response.
"""

import sys
import requests

def main(url, email):
    try:
        response = requests.post(url, data={'email': email})
        response.raise_for_status()  # Raise an HTTPError for bad responses
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    main(url, email)
