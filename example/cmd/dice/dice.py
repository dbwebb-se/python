#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example on a class rolling dices.

"""

import random


class Dice():
    """
    Example of class  with command actions.
    """
    def __init__(self):
        random.seed()


    def roll(self):
        """
        Move the turtle forward by the specified distance:  FORWARD 10
        """
        return random.randint(1, 6)
