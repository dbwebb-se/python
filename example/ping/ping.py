#!/usr/bin/env python3
"""
Simple test example of how to ping a website for a status code
http://stackoverflow.com/a/13641613
"""

url = "http://google.com/"

# module requests needs to be installed with pip
# http://docs.python-requests.org/en/latest/
# pip install requests
import requests
import time

try:
    # get current time
    rTime = time.ctime(time.time())
    # request header from url
    r = requests.head(url)
    # print result
    print ("Request to", url, "sent at", rTime)
    print("\t", r.status_code)
except requests.ConnectionError:
    print ("Failed to connect")
