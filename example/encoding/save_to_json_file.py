#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Save UTF to JSON file and then read it.
"""

import json


if __name__ == '__main__':
    print(__doc__)

    filename = "data.json"
    data = {"name": "Åsa Äppelöstad"}

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
        print("Saved UTF-8 characters to file: '{}'.".format(filename))

    with open(filename, "r", encoding="utf-8") as f:
        dataRead = json.load(f)
        print("Loaded file '{}'.".format(filename))
        print(dataRead)
