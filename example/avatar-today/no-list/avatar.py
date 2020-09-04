#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Keep a list of ASCII avatars and offer functions to use to present them.

All avatars are stored in variables, these variables are accessable
from outside of this module. That is how Python works.

You can run this script directly, and sending an extra argument on
the commandline. This is useful for testing modules.
"""

import sys
import time


garfield = r'''
                  --      --
                .:"  | .:'" |
              --  ___   ___  -
            /:.  / . \ / . \ .\
           |:|. ;\___/O\___/  :|
           |:|. |  `__|__'  | .|
           |:|.  \_,     ,_/  /
            \______       |__/
             |:.           \
            /.:,|  |        \
           /.:,.|  |         \
          |::.. \_;_\-;       |
     _____|::..    .::|       |
   /   ----,     .::/__,    /__,
   \_______|,...____;_;_|../_;_|
'''

odie = r'''
                                  .--"~~"    ~"\___
                                 Y              ]  ~~"\
                                 l   `v.,_    _/'      ]
                                  \   |   7~~"        /'
                                   \  |  / /~"------"~
                                 __.} l_/-^-<-.
                            .--"~      Y     I Y
                           /           l    oj-<______
                          Y       _     ~---~   (   ^ Y
                          l       |~t-.__(    // \.__.^
                           \      | |    ~\      _.^
                            "-._  | |      "---"~
                                Y |-^----------..,__
              .                 | |--.,__   --.,__  ~"-.
              \\                | l l    "~--.,_  ~--.  \
               \\    _____      |  \ \___,      "-._    /
                \>-"~     ~"-.--j   ~----/          "--"
                /        ,--.           Y
              _Y_ /     (    )     ___  |_      -Row
           ,-~   "       "--"     "   ~-< ~-.
          /                    Y         \   \
         /          /     .    l          Y  )Y
        /     l    /-.____l    !\,      ) ! / /
       Y    / /"--" /      \__/' \     / /_K-~
       `\__K-"\__.-"              ^.__K-"
'''

piglet = r'''
           ooooo                 oo
             $o"o$"o           o$$o$
              "$ $ $"o       o"$o $"o
               $"o"o"$o     o"$ $ $o$
               $"o"o$o$oooo$"o"o"o"o$
                ""o"  o "o $$ $"o""$
                 $o$   o  ""o$ $o$"
               o "   "o "o """$"
              o o$$"o"oo"" "o$"
             " $$ $  o"" o"oo"
             " """$ o  " o o"
             "o """"  o "o$
            oo $ooo "o o$$$
         o o" o$$$o$o$o$$$$ "o
     o " "  $o$$$$$$$$$$$$$o   o
   "  o o"$o$$$$$$$$$$$$$$$$ "  "o
 o" o o o"o"$$$$$$$$$$$$$$$$o$  o o
o  o o"o$" $$$$$$$$$$$$$$$$$$o$ o  "
o "o"o"   $$$$$$$$$$$$$o$$$$$ "$ $  $
"$o$"    $$$$$$$$$$$"$$$$$$$$   "o$ oo
        $$$$$$$$$$$$$$$$$$$$"     "$o"
        $$$$$$$$$$"$$$$$$$$$
         $$$$$$$$$$$$$$$$$$"
          $$$$$$"$$$$$$$$"
           "$$$$$$$$$$$$
            o  $"""""oo" o  o
            o"o" " ""o"o" o   o
            o"o"o o "o$"oo $ $"
              "" "" ""
'''

muppet = r'''
           .---.     .---.
          ( -o- )---( -o- )
          ;-...-`   `-...-;
         /                 \
        /                   \
       | /_               _\ |
       \`'.`'"--.....--"'`.'`/
        \  '.   `._.`   .'  /
     _.-''.  `-.,___,.-`  .''-._
    `--._  `'-._______.-'`  _.--`
    jgs  /                 \
        /.-'`\   .'.   /`'-.\
       `      '.'   '.'
'''

miss_muppet = r'''
           /  '.     .'  \
          | |`\ \,,,/ /`| |
           \.;;;;;-;;;;;./
          .;;;;-'"'"'-;;;;,
         ;;.-((((   ))))-.;;
       ,;;/ =/_o/___\o_\= \;;,
     ,;;;/    .-'   '-.    \;;;,
   ,;;;;/    /         \    \;;;;,
  ,;;;;|     \  \   /  /     |;;;;,
  ;;;;;\    /-`.__.__.`-\    /;;;;;
   ;;;;;\  `    \.-./    `  /;;;;;
    ;;;;;;-._  , '-' ,  _.-;;;;;;
     ';;;;/()`'-'-=-'-'`()\;;;;'
  jgs  `/`\ '()()()()()() /`\`
'''


def today():
    """Check the day and use its value to get an avatar."""
    which = round(time.time()) % 5 + 1
    return getAvatar(which)


def getAvatar(avatarId):
    """Get an avatar based on incoming avatarId."""
    if avatarId == 1:
        return(piglet)
    if avatarId == 2:
        return (muppet)
    if avatarId == 3:
        return (miss_muppet)
    if avatarId == 4:
        return (garfield)
    if avatarId == 5:
        return (odie)

    return 0


if __name__ == '__main__':
    print(__doc__)

    print("Extra arguments sent to this script.")
    print(sys.argv)
    print(getAvatar(int(sys.argv[1])))
