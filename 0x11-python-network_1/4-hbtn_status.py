#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print(
        "Body req:\n\t- type: {}\n\t- content: {}".format(
            type(req.text), req.text
        )
    )
