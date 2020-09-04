#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Show off how to scrape information from a webpage.
"""

from bs4 import BeautifulSoup
import requests



print(__doc__)
input("Press enter to continue. ")



# Get webpage
url = "https://dbwebb.se/irclog/"
print("\nReady to send HTTP request to ", url, "\nPress enter to continue. ", end='')
input()
req = requests.get(url)
print("\nThe response status code is:\n", req.status_code)



# Get the webpage content as a soup
#soup = BeautifulSoup(req.text, "html5lib")
soup = BeautifulSoup(req.text)

# Find the intresting parts in the soup
ircLog = soup.find("table")
logText = [element.text for element in ircLog.tr.findAll("td")] 

# Print out the content
formatString = "{} <{}> {}"
print("\nLast entry in IRC-log:")
print(formatString.format(*logText))
