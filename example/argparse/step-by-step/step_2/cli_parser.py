#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parse CLI options.

Basic 2, prints args and unknown_args
$ python3 cli_parser.py -h
$ python3 cli_parser.py hello
$ python3 cli_parser.py hello world
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("first")

args, unknown_args = parser.parse_known_args()

print("args: ", vars(args))
print("unknown_args: ", unknown_args)
