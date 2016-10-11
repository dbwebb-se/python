#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Roll a dice and see how it turns out.

This is sample code on how to use classes together with the
cmd-module to quickly create small CLI applications.

There is a class for the shell, that has callbacks for each commands.
That class is following a structure that the cmd-module expects.

There is a class representing the Dice. Just to act as a Dice.

The command module:
https://docs.python.org/3/library/cmd.html

"""

import diceshell


if __name__ == '__main__':
    print(__doc__)
    diceshell.Shell().cmdloop()
