#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main cli-program, to start it all up by reading command line
options and arguments and then executing whats to be executed.

$ python3 cli_parser.py -h
$ python3 cli_parser.py hello
$ python3 cli_parser.py hello world
"""

import sys
import cli_parser



def main():
    """
    Main function where it all starts.
    """

    options = cli_parser.parse_options()

    print(options)

    if options["args"]["first"]:
        print("Your input was: ", options["args"]["first"])

    sys.exit()

if __name__ == "__main__":
    main()
