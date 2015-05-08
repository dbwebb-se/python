#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example to show how command-line options can be handled by a script.
"""



import sys
import os
from datetime import datetime
import getopt



#
# Add some stuff about this script
#
PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Mikael Roos"
EMAIL = "mikael.t.h.roos@gmail.com"
VERSION = "1.0.1"
USAGE = """{program} - Print my name. By {author} ({email}), version {version}.

Usage:
  {program} [options] name

Options:
  -d <number> --drum=<number>   Make a drum sound when writing the name.
  -h --help                      Display this help message.
  -r <number> --repeat=<number>  Print the name several times.
  -s --silent                    Do not display any details or statistics about the execution.
  -v --version                   Print version and exit.

  name                           Your name.
""".format(program=PROGRAM, author=AUTHOR, email=EMAIL, version=VERSION)

MSG_VERSION = "{program} version {version}.".format(program=PROGRAM, version=VERSION)
MSG_USAGE = "Use {program} --help to get usage.\n".format(program=PROGRAM)




#
# Global default settings affecting behaviour of script in several places
#
REPEAT = 0
DRUM = 0
SILENT = False
VERBOSE = True
NAME = ""

EXIT_SUCCESS = 0
EXIT_USAGE = 1
EXIT_FAILED = 2



def printUsage(exitStatus):
    """
    Print usage information about the script and exit.
    """
    print(USAGE)
    sys.exit(exitStatus)



def printVersion():
    """
    Print version information and exit.
    """
    print(MSG_VERSION)
    sys.exit(EXIT_SUCCESS)



def printMyName():
    """
    Print the name.
    """

    print("My name is ", end="")

    if DRUM:
        print(NAME[0:1] * DRUM, end="")

    print(NAME, end="")
    print(NAME * REPEAT, end="")
    print("!")



def parseOptions():
    """
    Merge default options with incoming options and arguments and return them as a dictionary.
    """

    # Switch through all options
    try:
        global DRUM, REPEAT, VERBOSE

        opts, args = getopt.getopt(sys.argv[1:], "d:hr:sv", ["drum=", "help", "repeat=", "version", "silent"])

        for opt, arg in opts:
            if opt in ("-d", "--drum"):
                if not arg.isnumeric():
                    assert False, "-d, --drum: {arg} is not a numeric value".format(arg=arg)

                DRUM = int(arg)

                if VERBOSE:
                    print("Setting DRUM to ", DRUM)

            elif opt in ("-h", "--help"):
                printUsage(EXIT_SUCCESS)

            elif opt in ("-r", "--repeat"):
                if not arg.isnumeric():
                    assert False, "-r, --repeat: {arg} is not a numeric value".format(arg=arg)

                REPEAT = int(arg)

                if VERBOSE:
                    print("Setting REPEAT to ", REPEAT)

            elif opt in ("-s", "--silent"):
                VERBOSE = False

            elif opt in ("-v", "--version"):
                printVersion()

            else:
                assert False, "Unhandled option"

        if len(args) != 1:
            assert False, "Missing name"

        # The name passed as a required argument
        global NAME
        NAME = args[0]

    except Exception as err:
        print(err)
        print(MSG_USAGE)
        # Prints the callstack, good for debugging, comment out for production
        #traceback.print_exception(Exception, err, None)
        sys.exit(EXIT_USAGE)




def main():
    """
    Main function to carry out the work.
    """
    startTime = datetime.now()

    parseOptions()

    printMyName()

    timediff = datetime.now()-startTime
    if VERBOSE:
        sys.stderr.write("Script executed in {}.{} seconds\n".format(timediff.seconds, timediff.microseconds))

    sys.exit(EXIT_SUCCESS)



if __name__ == "__main__":
    main()
