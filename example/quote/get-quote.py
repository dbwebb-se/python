#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Get a random quote from a webservice and print it out. 

The webservice in the example is:
http://dbwebb.se/javascript/lekplats/get-marvin-quotes-using-ajax/quote.php
"""

import requests



print(__doc__)
input("Press enter to continue. ")


url = "http://dbwebb.se/javascript/lekplats/get-marvin-quotes-using-ajax/quote.php"


try:

    print("\nReady to send HTTP request to ", url, "\nPress enter to continue. ", end='')
    input()
    req = requests.get(url)

    print("\nThe response status code is:\n", req.status_code)

    print("\nThe response body is:\n", req.text)

    json = req.json()
    print("\nQuote of today is:\n\"{quote}\"\n".format(quote=json["quote"]))


except requests.ConnectionError:

    print("Failed to connect.")
