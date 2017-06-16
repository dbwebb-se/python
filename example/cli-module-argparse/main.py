#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main cli-program, to start it all up by reading command line
options and arguments and the executing whats to be executed.

See usage.py for details how to use program.
>>> import usage
>>> help(usage)

or 

$ pydoc usage

"""

import sys
import usage_module


def main():
    """
    Main function where it all starts.
    """
    usage_module.parse_options()

    print("Default options:")
    print(usage_module.default_options)

    print("Active options:")
    print(usage_module.options)
    print()

    sys.exit()


if __name__ == "__main__":
    main()
