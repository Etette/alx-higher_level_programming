#!/usr/bin/python3
"""
Script takes 'q'and sends a POST rrequest
to 0.0.0.0:5000/search_user with 'q' as
param.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/seaarch_user'
    value = argv[1] if len(argv) > 1 else ""
    req = requests.post(url, data={'q': value})
    try:
        _dict = req.json()
        if _dict == {}:
            print('No result')
        else:
            print("[{}] {}".format(_dict.get('id'), _dict.get('name')))
    except ValueError:
        print('Not a valid JSON')
