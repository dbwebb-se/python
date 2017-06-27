#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parse CLI options and return as dict.

Present usage and version information.

Usage and parsing options.

Exit status:
0 EXIT_SUCCESS success
1 EXIT_USAGE   failed parsing cli options
2 EXIT_FAILED  Execution error
"""

import os
import sys
import getopt



#
# Add basics about this program
#
PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Your Name"
EMAIL = "your@email"
VERSION = "v1.0.0 (2017-06-15)"

MSG_USAGE = """{program} - short description on what this command does.
By {author} ({email}), version {version}.

Usage:
  {program} [options] <command>

options:
  -h, --help                         Display this help message.
  -v, --version                      Print version and exit.
  --silent                           Decrease verbose output.
  --verbose                          Increase verbose output.
""".format(
    program=PROGRAM,
    author=AUTHOR,
    email=EMAIL,
    version=VERSION
)

MSG_VERSION = "{version}".format(version=VERSION)

MSG_HELP = "Use {program} --help to get usage.".format(program=PROGRAM)


#
# Global default settings affecting behaviour of script in several places
#
EXIT_SUCCESS = 0
EXIT_USAGE = 1
EXIT_FAILED = 2



default_options = {
    "verbose": False,
    "silent": False,
    "commands": None
}

options = default_options.copy()

def print_usage(exit_status=0):
    """Print usage information about the script and exit."""
    print(MSG_USAGE)
    sys.exit(exit_status)

def print_version():
    """Print version information and exit."""
    print(MSG_VERSION)
    sys.exit()

def parse_options(argv=None):
    """
    Parse all command line options and arguments.

    Return them as a dictionary.
    """
    
    
    argv = argv if argv is not None else sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "hv", [
            "help",
            "version",
            "silent",
            "verbose"
        ])

        for opt, _ in opts:
            if opt in ("-h", "--help"):
                print_usage()

            elif opt in ("-v", "--version"):
                print_version()

            elif opt in "--silent":
                options["silent"] = True

            elif opt in "--verbose":
                options["verbose"] = True
        
        
        options["commands"] = args
            

    except getopt.GetoptError as err:
        print(err)
        print(MSG_HELP)
        sys.exit(EXIT_USAGE)
