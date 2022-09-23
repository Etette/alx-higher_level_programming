#!/usr/bin/python3
"""
Scriptprints last 10 commits from
a github user using github API
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    rep = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, rep)
    req = requests.get(url)
    count = 0

    for i in req.json():
        print(i.get('sha') + ": " + i.get('commit').get('author').get('name'))
        count += 1
        if count == 10:
            break
