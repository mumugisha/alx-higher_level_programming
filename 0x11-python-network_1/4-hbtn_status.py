#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import sys
import requests

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body Response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
