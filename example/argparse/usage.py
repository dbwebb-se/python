#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parse CLI options. This is a standalone file.

Using argparse to parse options.

Exit status:
0 EXIT_SUCCESS success
1 EXIT_USAGE   failed parsing cli options
2 EXIT_FAILED  Execution error
"""

# import os
# import sys
import argparse

#
# Add basics about this program
#
# PROGRAM = os.path.basename(sys.argv[0])
PROGRAM = "This is a cli-module"
AUTHOR = "Your Name"
EMAIL = "your@email"
VERSION = "v1.0.0 (2017-06-16)"

default_options = {
    "verbose": False,
    "silent": False,
    "commands": None
}

options = default_options.copy()

def print_info():
    """Print usage information about the script."""
    return "By {author} ({email}), version {version}".format(
        author=AUTHOR,
        email=EMAIL,
        version=VERSION
    )

def parse_options():
    """
    Parse all command line options and arguments.

    Return them as a dictionary.
    """
    parser = argparse.ArgumentParser(prog=PROGRAM, description=print_info())
    group = parser.add_mutually_exclusive_group()

    group.add_argument("--verbose", dest="verbose", help="increase output verbosity", action="store_true")
    group.add_argument("--silent", dest="silent", help="decrease output verbosity", action="store_true")

    parser.add_argument("-v", "--version", action="version", version=VERSION)

    args, unknownargs = parser.parse_known_args()

    if args.verbose:
        options["verbose"] = True
        
    if args.silent:
        options["silent"] = True
    
    options["commands"] = unknownargs
    
    return options
