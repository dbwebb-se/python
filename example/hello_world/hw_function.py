#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A function to say Hello, just to show off how functions and docstrings works.

Use it like this.

>>> import hw_function as hw
>>> help(hw)
>>> hw.say_it.__doc__
>>> hw.__doc__

Also try pydoc like this in the terminal:

pydoc sys

"""



def say_it():
    """
    Just sayin to the world that we are here and now know python.

    Ths function is currently defined in a module named __name__.
    """
    print("\nHello World in module %s\n" % __name__)

