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

verbose_text = """
You have chosen to use the --verbose option.
Your input was: {input}
Unknown arguments: {unknown}
Thank you and good bye!
"""

def main():
    """
    Main function where it all starts.
    """

    options = cli_parser.parse_options()
    command = options["args"]
    silent = options["args"]["silent"]
    verbose = options["args"]["verbose"]

    if command["first"]:
        if silent:
            print(command["first"])
        elif verbose:
            print(verbose_text.format(input=command["first"], unknown=options["unknown_args"]))
        else:
            print("Your input was:", command["first"])

    sys.exit()

if __name__ == "__main__":
    main()
