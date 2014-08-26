#!/usr/bin/env python3
"""
Test to scarpe a webpage
It is possible to pass an arugment when running the program
    to filter out channels, for example:
./tv-tabla.py svt
Used:
http://dbwebb.se/forum/viewtopic.php?f=41&t=2305
http://stackoverflow.com/a/2082025
http://www.crummy.com/software/BeautifulSoup/#Download
"""

import sys
# http://stackoverflow.com/a/6594775
try:
    import urllib.request as urllib2
except:
    import urllib2
# if you're using BeautifulSoup4:
from bs4 import BeautifulSoup

# argument from command line
if len(sys.argv) == 2:
    CHANNEL = sys.argv[1]
else:
    CHANNEL = ""

# Link
TV = "http://www.tv.nu/"

# soup
soup = BeautifulSoup(urllib2.urlopen(TV))

def getTabla(theSoup):
    """
    Uses the soup to filter out current shows on TV
    """
    for row in theSoup("div", {"class": "tabla_container"}):
        for title in row("p", {"class": "tabla_topic_label"}):
            if CHANNEL.lower() in title.text.lower():
                print(title.text.strip())
                for current in row("li", {"class": "po"}):
                    print("\t", current.text.strip(), "-", current.a.text.strip())
                print("-----")
            else:
                break

getTabla(soup)