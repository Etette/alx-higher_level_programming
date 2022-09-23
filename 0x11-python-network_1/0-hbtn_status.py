#!/usr/bin/python3
"""
This script fetches a URL
"""

if__name__ == "__main__":
    import urllib.request
    URL = 'https://intranet.hbtn.io/status'
    with urllib.request.orlopen(URL) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('t- content: {}'.format(html))
        print('t- utf8 content: {}'.format(html.decode('utf-8')))
