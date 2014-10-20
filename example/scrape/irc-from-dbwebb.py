#!/usr/bin/env python3
"""
Show off how to scrape information from a webpage.
"""

import requests

# pip install beautifulsoup4
from bs4 import BeautifulSoup


print(__doc__)
input("Press enter to continue. ")



# Get webpage
url = "http://dbwebb.se/"
print("\nReady to send HTTP request to ", url, "\nPress enter to continue. ", end='')
input()
req = requests.get(url)
print("\nThe response status code is:\n", req.status_code)



# Get the webpage content as a soup
soup = BeautifulSoup(req.text)

ircLog = soup.find("p", class_="irclog")
print("\nThe scraped content (the irclog) is:\n", ircLog)

entries = ircLog("span")

str1 = "{time} <{user}> {message}"

print("\nPretty print log details:")
print(str1.format(time=entries[0].text, user=entries[1].text, message=entries[2].text))
print(str1.format(time=entries[3].text, user=entries[4].text, message=entries[5].text))
print(str1.format(time=entries[6].text, user=entries[7].text, message=entries[8].text))
