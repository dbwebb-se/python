#!/usr/bin/env python3

# import socket

# from urllib.request import urlopen, URLError, HTTPError

# socket.setdefaulttimeout( 23 )  # timeout in seconds

url = 'http://google.com/'
# try :
#     response = urlopen( url )
# except (HTTPError, e):
#     print ('The server couldn\'t fulfill the request. Reason:', str(e.code))
# except (URLError, e):
#     print ('We failed to reach a server. Reason:', str(e.reason))
# else :
#     # html = response.read()
#     print(response.getcode())
#     # do something, turn the light on/off or whatever

# ----------------------------------------------
import requests
import time

try:
    rTime = time.time()
    r = requests.head(url)
    print ("Request to", url, "sent at", time.ctime(rTime))
    print("\t", r.status_code, "(Repsonse time:", r.elapsed.total_seconds(), "s)")
    #prints the int of the status code. Find more at httpstatusrappers.com :)
except requests.ConnectionError:
    print ("failed to connect")

