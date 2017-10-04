#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Read options and arguments from command line and supply to program.

Using argparse to parse options and arguments.
"""

import argparse

VERSION = "v1.0.0 (2017-10-03)"


def parse_options():
    """Parse command line options/arguments and return them as a dictionary."""
    parser = argparse.ArgumentParser(
        description="Make an ascii painting."
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=VERSION
    )
    parser.add_argument(
        "-s", "--silent",
        action="store_true",
        help="be more silent."
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="be more verbose."
    )
    parser.add_argument(
        "filename",
        help="path to JSON configuration file."
    )

    return vars(parser.parse_args())


if __name__ == "__main__":
    pass
