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


print("Number of options: {}".format(len(opts)))
print("Number of arguments: {}".format(len(args)))

print(opts)
print(args)
