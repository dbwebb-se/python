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

import os
import sys
import argparse

#
# Add basics about this program
#
PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Your Name"
EMAIL = "your@email"
VERSION = "v1.0.0 (2017-06-16)"

def print_info():
    """Print usage information about the script."""
    return "By {author} ({email}), version {version}".format(
        author=AUTHOR,
        email=EMAIL,
        version=VERSION
    )

parser = argparse.ArgumentParser(prog=PROGRAM, description=print_info(), formatter_class=argparse.RawTextHelpFormatter)

subparsers = parser.add_subparsers(title="commands (positional arguments)", help='Available commands', dest="command")
subparsers.add_parser("sum", help="[integers]   display the sum of the given numbers")
subparsers.add_parser("sub", help="[integers]   display the subtraction of the first two given numbers")
subparsers.add_parser("square", help="[integers]   display the square of the given numbers")

parser.add_argument("-s", "--silent", help="decrease output verbosity", action="store_true")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-V", "--version", action="version", version=VERSION)


args, unknown_args = parser.parse_known_args()

answer = ""

unknown_args = list(map(int, unknown_args))

if args.command == "sum" and unknown_args:
    result = str(sum(unknown_args))
    answer = result
    if args.verbose:
        answer = "The sum of {} is: {}".format(", ".join(str(number) for number in unknown_args), result)

elif args.command == "square" and unknown_args:
    for square_me in unknown_args:
        result = str(square_me**2)
        square_me = str(square_me)
        if args.verbose:
            answer += "{}^2 == {}\n".format(square_me, result)
        else:
            answer += result + "\n"

elif args.command == "sub" and unknown_args:
    left_hand = unknown_args[0]
    right_hand = unknown_args[1]
    result = left_hand - right_hand
    
    if args.verbose:
        answer = "The result of {}-{} is: {}".format(left_hand, right_hand, result)
    else:
        answer = result

print(answer)
