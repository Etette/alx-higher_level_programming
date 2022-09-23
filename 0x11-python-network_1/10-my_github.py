#!/usr/bin/python3
"""
Script takes Github cred and api
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    user = argv[1]
    psswd = argv[2]
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(user, psswd))
    print(req.json().get('id'))
