#!/usr/bin/env python3
"""
Simple test example of how to ping a website for a status code
"""

url = 'http://google.com/'

import requests
import time

try:
    rTime = time.ctime(time.time())
    r = requests.head(url)
    print ("Request to", url, "sent at", rTime)
    print("\t", r.status_code)
except requests.ConnectionError:
    print ("failed to connect")
