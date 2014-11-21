#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Show off how to read string from keyboard when in curses.
"""

import curses


def main(scr):
    """
    Enter a string, while echoing to the window. Press enter and the string is echoed to the 
    screen. Press a character to exit the program while the string being returned and printed
    by the caller.
    """
    
    # Clear the screen of any output
    scr.clear()

    # Draw a border
    scr.border()

    # Move cursor to center
    scr.move(1, 1)

    # Refresh to draw out
    scr.refresh()

    # Get a string from the user
    curses.echo();
    str = scr.getstr()
    scr.move(2, 2)
    scr.addstr(str)
    scr.refresh()

    # Wait for user input.
    scr.getch();
    return str


if __name__ == "__main__":
    print(__doc__)
    print(main.__doc__)
    input("Press enter to begin playing...")
    str = curses.wrapper(main)
    print(str)

