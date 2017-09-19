#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Keep a list of ASCII avatars and offer functions to use to present them.

The avatars are stored in a list that is accessable
from outside of this module. That is how Python works.

You can run this script directly, and sending an extra argument on
the commandline. This is useful for testing modules.
"""

import sys
import time
import os

avatars = []
# files = [
#     "garfield",
#     "odie",
#     "piglet",
#     "muppet",
#     "miss_muppet"
# ]
#
# for avatar in files:
#     filename = "avatar/" + avatar + ".txt"
#     with open(filename) as f:
#         string = f.read()
#         avatars.append(string)

avatar_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "avatar"
)
for avatar_filename in os.listdir(avatar_path):
    filename = os.path.join(avatar_path, avatar_filename)
    with open(filename) as f:
        string = f.read()
        avatars.append(string)


def today():
    """Check the day and use its value to get an avatar."""
    which = round(time.time()) % len(avatars) + 1
    return getAvatar(which)


def getAvatar(avatarId):
    """Get an avatar based on incoming avatarId."""
    return avatars[avatarId % len(avatars)]


if __name__ == '__main__':
    print(__doc__)

    print("Extra arguments sent to this script.")
    print(sys.argv)
    print(getAvatar(int(sys.argv[1])))
