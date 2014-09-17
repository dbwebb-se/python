#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example of how to ping a webpage for a status code, basically just
to check that the page is there and the webserver is replying with 
a positive code, such as 200.

More information: http://stackoverflow.com/a/13641613

The module requests needs to be installed with pip
http://docs.python-requests.org/en/latest/
pip install requests
"""

print(__doc__)

import requests
import time


url = "http://dbwebb.se/humans.txt"


try:

    # Get current time
    rTime = time.ctime(time.time())

    # Request header from url
    print("Ready to send HTTP request to ", url, "\n(press return)", end='')
    input()
    req = requests.head(url)

    # Print result
    print("Request to ", url, " sent at ", rTime)
    print("Recieved status code: ", req.status_code)
    print("Page was last modified: ", req.headers["Last-Modified"])



except requests.ConnectionError:

    print("Failed to connect")
