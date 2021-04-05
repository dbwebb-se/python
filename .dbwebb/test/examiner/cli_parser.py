"""
Parses all custom options and arguments
"""
import argparse

def parse():
    """
    Handles the arguments and options.
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)

    # absolute path to the test folder
    parser.add_argument(
        "-w", "--what", dest="what", required=True,
        help="REQUIRED - The absolute path to the folder containing the tests"
    )

    # create the parser for the "tags" command
    parser.add_argument(
        "-t", "--tags", dest="tags", default=[],
        help="Collects tags to run specific tests\n" + \
            "USAGE: -t=tag1 || -t=tag1,tag2"
    )

    # create the parser for the extra command
    parser.add_argument(
        "-e", "--extra", dest="extra_assignments", default=False,
        action="store_true", help="Includes tests for extra assignments"
    )

    args, _empty = parser.parse_known_args()

    if args.tags:
        args.tags = args.tags.split(",")

    return args
