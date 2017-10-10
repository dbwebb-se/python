#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parse CLI options.
Basic 4, prints args and unknown_args with --silent and --verbose
"""

import argparse

options = {}

def parse_options():

    parser = argparse.ArgumentParser()

    parser.add_argument("--silent", dest="silent", action="store_true")
    parser.add_argument("--verbose", dest="verbose", action="store_true")

    parser.add_argument("first")

    args, unknown_args = parser.parse_known_args()

    options["args"] = vars(args)
    options["unknown_args"] = unknown_args

    return options
