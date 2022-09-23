#!/usr/bin/python3
"""
Scrpt taskes a url, sends request to url
and displays the value of X-Request-Id
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    value = 'X-Requests-Id'
    html = requests.get(url)
    print(html.headers.get(value))
