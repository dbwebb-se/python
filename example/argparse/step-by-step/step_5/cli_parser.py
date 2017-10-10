#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parse CLI options.
Basic 5, using subparser
"""

import argparse

options = {}

def parse_options():

    parser = argparse.ArgumentParser()

    parser.add_argument("--silent", dest="silent", action="store_true")
    parser.add_argument("--verbose", dest="verbose", action="store_true")

    subparsers = parser.add_subparsers(title="commands (positional arguments)", help='Available commands', dest="command")

    subparsers.add_parser("hello", help="Respons to hello");
    subparsers.add_parser("goodbye", help="Respons to goodbye");


    args, unknown_args = parser.parse_known_args()

    options["args"] = vars(args)
    options["unknown_args"] = unknown_args

    return options
