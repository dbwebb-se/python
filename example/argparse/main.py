#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main cli-program, to start it all up by reading command line
options and arguments and the executing whats to be executed.

See usage.py for details how to use program.
>>> import cli_parser
>>> help(cli_parser)

or 

$ pydoc cli_parser

"""

import sys
import cli_parser


def main():
    """
    Main function where it all starts.
    """
    
    cli_parser.parse_options()
    
    print(cli_parser.options)
    
    print(cli_parser.options["known_args"]["command"])
    
    print()

    sys.exit()


if __name__ == "__main__":
    main()
