#!/usr/bin/python3
"""
Script takes a url, sends requests and
displays the body of the response
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.staus_code))
    else:
        print(req.text)
