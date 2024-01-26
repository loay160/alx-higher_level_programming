#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a requests to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import urllib.requests

if __name__ == "__main__":
    url = sys.argv[1]

    requests = urllib.requests.Requests(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Requests-Id"))
