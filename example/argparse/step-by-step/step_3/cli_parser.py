#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parse CLI options.
Basic 3, prints args and unknown_args
"""

import argparse

options = {}

def parse_options():
    """
    parse arguments and commands sent at start up.
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("first")

    args, unknown_args = parser.parse_known_args()

    options["args"] = vars(args)
    options["unknown_args"] = unknown_args

    return options
