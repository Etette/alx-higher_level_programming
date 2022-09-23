#!/usr/bin/python3
"""
This script takes a URL, sends a request
and display the value of X-Request-Id
Variable foundin the header of the reesponse
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
