#!/usr/bin/python3
"""
Script takes a url and email addrs,
sends a POST request to url with email
as param and finally displays the body of
the response
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    email = argv[2]
    values = {'email': email}
    request = requests.post(url, data=values)
    print(request.text)
