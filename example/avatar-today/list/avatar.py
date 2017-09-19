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

avatars = []
avatars.append(r'''
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
''')

avatars.append(r'''
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
''')

avatars.append(r'''
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
''')

avatars.append(r'''
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
''')

avatars.append(r'''
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
''')


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
