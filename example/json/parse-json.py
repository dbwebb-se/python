#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testing out reading and writing json to a file
"""

import os.path
import json


# Create a file object
filename = "json.txt"
filenameMy = "json-mine.txt"

# Check if my own file exists, else use the default one
if os.path.isfile(filenameMy):
    filename = filenameMy


# Read from file and decode as json
with open(filename, "r") as fd:
    jsonobject = json.load(fd)


# Print out the content from the dict
for color in jsonobject["colorsArray"]:
    print(color["colorName"], color["hexValue"])


# Ask if color is to be added
confirm = input("Do you want to add a color (y/n)? ")


if confirm.lower() == "y":

    # Get new color
    colorName = input("Enter color name: ")
    hexValue = input("Enter hex value (with #): ")

    # append the color as a dict to the colorsarray
    jsonobject["colorsArray"].append({
        "colorName": colorName,
        "hexValue": hexValue
    })

    # Open the file for writing ("w" will replace the file contents)
    # Encode json with pretty output (indent)
    with open(filenameMy, "w") as fd:
        json.dump(jsonobject, fd, indent=4)
