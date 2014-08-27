#!/usr/bin/env python3
"""
Testing out reading a writing json to a file
"""

import json

# Open file and read all its contents
fhand = open("json.txt", "r")
content = fhand.read()
fhand.close()

# Decode json
stuff = json.loads(content)

# Print out the content from the dict
for color in stuff["colorsArray"]:
    print(color["colorName"], color["hexValue"])

# Ask if color is to be added
confirm = input("Do you want to add a color (y/n)? ")

if confirm.lower() == "y":
    # get new color
    colorName = input("Enter color name: ")
    hexValue = input("Enter hex value (with #): ")

    # append the color as a dict to the colorsarray
    stuff["colorsArray"].append({
        "colorName": colorName,
        "hexValue": hexValue
    })

    # Open the file for writing ("w" will replace the file contents)
    fhand = open("json.txt", "w")
    # Encode json with pretty output (indent)
    fhand.write(json.dumps(stuff, indent = 4))
    fhand.close()