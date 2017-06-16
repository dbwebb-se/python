#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parse CLI options and return as dict.

Present usage and version information.

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

parser = argparse.ArgumentParser(prog=PROGRAM, description=print_info())
group = parser.add_mutually_exclusive_group()

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='integers to use in calculation')

group.add_argument("--sum", dest="accumulate", help="display the sum of the given numbers", action="store_true")
group.add_argument("--square", help="display the square of the given numbers", action="store_true")
group.add_argument("--sub", help="display the subtraction of the first two given numbers", action="store_true")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-V", "--version", action="version", version=VERSION)

args = parser.parse_args()

answer = ""

if args.accumulate and args.integers:
    result = str(sum(args.integers))
    answer = result
    if args.verbose:
        answer = "The sum of {} is: {}".format(", ".join(str(number) for number in args.integers), result)

if args.square and args.integers:
    for square_me in args.integers:
        result = str(square_me**2)
        square_me = str(square_me)
        if args.verbose:
            answer += "{}^2 == {}\n".format(square_me, result)
        else:
            answer += result + "\n"

if args.sub and args.integers:
    left_hand = args.integers[0]
    right_hand = args.integers[1]
    result = left_hand - right_hand
    
    if args.verbose:
        answer = "The result of {}-{} is: {}".format(left_hand, right_hand, result)
    else:
        answer = result

print(answer)
