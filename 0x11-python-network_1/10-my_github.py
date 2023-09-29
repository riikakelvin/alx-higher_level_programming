#!/usr/bin/python3
"""
Module Docstring
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://api.github.com/user"
    user = argv[1]
    pwd = argv[2]

    r = requests.get(url, headers={'Authorization': 'token {}'.format(pwd)})
    try:
        print(r.json()['id'])
    except KeyError:
        print("None")
