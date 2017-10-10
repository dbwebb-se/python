#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main cli-program, to start it all up by reading command line
options and arguments and then executing whats to be executed.

$ python3 main.py -h
$ python3 main.py hello
$ python3 main.py goodbye
$ python3 main.py --verbose hello world
$ python3 main.py --silent goodbye world

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
    command = options["args"]["command"]
    silent = options["args"]["silent"]
    verbose = options["args"]["verbose"]

    if command == "hello":
        if silent:
            print("Hi!")
        elif verbose:
            print(verbose_text.format(input=command, unknown=options["unknown_args"]))
        else:
            print("This is a response to the command: " + command + ":\nHello there!")

    if command == "goodbye":
        if silent:
            print("Bye!")
        elif verbose:
            print(verbose_text.format(input=command, unknown=options["unknown_args"]))
        else:
            print("This is a response to the command: " + command + ":\nGoodbye!")

    sys.exit()

if __name__ == "__main__":
    main()
