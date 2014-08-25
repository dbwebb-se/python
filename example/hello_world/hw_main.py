#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Calling the function what says hello from a main-method and using docstrings
to document it all. Showing how to import a file (module) with an external
function.

Import it and run it by calling the main function or run it as a script.

1) In the python interpreter

>>> import hw_main as hw
>>> hw.main()


2) In the shell

$ python3 hw_main.py


3) Make it executable and just run it.

$ chmod 755 hw_main.py
$ ./hw_main.py

"""

import hw_function as hw


def main():
    """
    This is the main method, I call it main by convention.
    """
    print(hw.say_it.__doc__)
    hw.say_it()



if __name__ == "__main__":
    print(main.__doc__)
    main()

