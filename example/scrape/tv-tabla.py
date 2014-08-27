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
except ImportError:
    import urllib2
# pip install beautifulsoup4
from bs4 import BeautifulSoup

# argument from command line
if len(sys.argv) == 2:
    CHANNEL = sys.argv[1]
else:
    CHANNEL = ""

# Link
TV = "http://www.tv.nu/"

# Get the webpage content as a soup
soup = BeautifulSoup(urllib2.urlopen(TV))

def getTabla(theSoup):
    """
    Uses the soup to filter out current shows on TV
    """
    # Get the container for each channel
    for row in theSoup("div", {"class": "tabla_container"}):
        # Get the title of each channel
        for title in row("p", {"class": "tabla_topic_label"}):
            # Continue if the title is a match to input or everything ("")
            if CHANNEL.lower() in title.text.lower():
                print(title.text.strip())
                # Get the current program
                for current in row("li", {"class": "po"}):
                    print("\t", current.text.strip(), "-", current.a.text.strip())
                print("-----")
            else:
                break

getTabla(soup)