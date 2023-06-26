#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example to show how module cmd is use.

Error handling is partly missing by intent.

"""

import cmd
import dice

# _pylint: disable=locally-disabled,unused-argument,too-many-public-methods
# pylint: disable=locally-disabled,unused-argument


class Shell(cmd.Cmd):
    """
    Example of class with command actions to roll a dice.
    """
    intro = 'Welcome to the dice shell. Type help or ? to list commands.\n'
    prompt = '(dice) '


    def __init__(self):
        super().__init__()
        self.dice = dice.Dice()


    def do_roll(self, arg):
        """
        Roll one dice one time.
        """
        print(f"Rolling a... {self.dice.roll()}")


    def do_rolls(self, arg):
        """
        Roll one dice several times, supply argument how many times to roll.
        """
        if not arg:
            print("Missing argument on how many times to roll the dice.")
            return

        times = int(arg)
        for _ in range(times):
            print(f"Rolling a... {self.dice.roll()}")


    def do_total(self, arg):
        """
        How many rolls have been made in total?
        """
        print(f"You have rolled the dice {self.dice.getRollsMade()} times.")


    def do_exit(self, arg):
        """
        Leave the game.
        """
        print("Bye bye - see ya soon again")
        return True
