#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parse CLI options.

Basic, prints args and unknown_args
Try it:
$ python3 cli_parser.py -h
$ python3 cli_parser.py hej
"""

import argparse

parser = argparse.ArgumentParser()

args, unknown_args = parser.parse_known_args()

print("args: ", vars(args))
print("unknown_args: ", unknown_args)
