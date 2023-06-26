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
        print(f"Saved UTF-8 characters to file: '{filename}'.")

    with open(filename, "r", encoding="utf-8") as f:
        dataRead = json.load(f)
        print(f"Loaded file '{filename}'.")
        print(dataRead)
