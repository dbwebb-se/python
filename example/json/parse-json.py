#!/usr/bin/env python3
"""
Testing out reading a writing json to a file
"""

import json

fhand = open("json.txt", "r")
line = fhand.readline()
fhand.close()


stuff = json.loads(line)

for color in stuff["colorsArray"]:
    print(color["colorName"], color["hexValue"])

colorName = input("Enter color name: ")
hexValue = input("Enter hex value (with #): ")

stuff["colorsArray"].append({
    "colorName": colorName,
    "hexValue": hexValue
})


fhand = open("json.txt", "w")
fhand.write(json.dumps(stuff))
fhand.close()