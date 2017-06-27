#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parse CLI options.

Using argparse to parse options.
"""

import argparse

VERSION = "v1.0.0 (2017-06-16)"

options = {}

def parse_options():
    """
    Parse all command line options and arguments and return them as a dictionary.
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-v", "--verbose", dest="verbose", default="False",
                       help="increase output verbosity", action="store_true")
    group.add_argument("-s", "--silent", dest="silent", default="False",
                       help="decrease output verbosity", action="store_true")

    parser.add_argument("-V", "--version", action="version", version=VERSION)
    
    subparsers = parser.add_subparsers(
        title="commands (positional arguments)", 
        help='Available commands', 
        dest="command")
    subparsers.add_parser("command1", help="information on command1")
    subparsers.add_parser("command2", help="information on command2")



    args, unknownargs = parser.parse_known_args()

    options["known_args"] = vars(args)
    options["unknown_args"] = unknownargs
    
    return options
