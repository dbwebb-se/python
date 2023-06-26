#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Print out the options and arguments.
"""


import sys
import getopt


opts, args = getopt.getopt(sys.argv[1:], "hv", [
    "help",
    "version"
])


print(f"Number of options: {len(opts)}")
print(f"Number of arguments: {len(args)}")

print(opts)
print(args)
