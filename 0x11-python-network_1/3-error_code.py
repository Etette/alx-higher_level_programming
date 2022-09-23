#!/usr/bin/python3
"""
Script takes a url, sends a request
and dusplays body encode=utf-8
Manage urllib.error.HTTPerror exception
"""

if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPerror
    import sys

    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPerror as error:
        print("Error code: {}".format(error.code))
