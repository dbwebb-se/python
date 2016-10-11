#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example on a class rolling dices.

"""

import random


class Dice():
    """
    Example of dice class.
    """
    faces = 6


    def __init__(self):
        random.seed()
        self.rollsMade = 0


    def roll(self):
        """
        Roll a dice once and return the value.
        """
        self.rollsMade += 1
        return random.randint(1, self.faces)


    def getRollsMade(self):
        """
        Get number of rolls made.
        """
        return self.rollsMade
