#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Move around a pad on screen using arrow-keys or keys "asdw".
"""

import time
import curses


def drawPad(scr, pad, char=''):
    """
    Draw the pad at its position.
    """
    x, y = pad["x"], pad["y"]

    # The caller can change the char representing the pad
    if char == '':
        char = pad["char"]

    for _ in range(pad["width"]):
        scr.addstr(y, x, char)
        x += 1



def movePad(scr, pad, x, y):
    """
    Move and re-draw the pad.
    """

    # Clear the pad
    drawPad(scr, pad, ' ')

    # Move the pad
    pad["x"] += x
    pad["y"] += y

    # Re-draw the pad
    drawPad(scr, pad)

   

def main(scr):
    """
    Draw a pad and move it around.

    Press any key to quit.
    """

    # Don't stop the while-loop while waiting for input
    scr.nodelay(1)

    # Draw a border
    scr.border()

    # Make cursor invisible
    curses.curs_set(0)

    # Use a dictionary as datastructure for the pad
    pad = {
        "char": "=",
        "width": 6,
        "x": 0,
        "y": 0
    }

    # Get dimensions
    max_y, max_x = scr.getmaxyx()

    # Starting position
    pad["x"] = max_x // 2
    pad["y"] = max_y // 2

    # Draw the pad
    drawPad(scr, pad)
    scr.refresh()

    # Do until exit
    while True:

        # Get input from user and flush the input buffer
        ch = scr.getch()
        curses.flushinp()
        
        # Check if a key was pressed and update
        if ch == curses.KEY_LEFT or ch == ord('a'):
            movePad(scr, pad, -1, 0)

        elif ch == curses.KEY_RIGHT or ch == ord('d'):
            movePad(scr, pad, 1, 0)

        elif ch == curses.KEY_UP or ch == ord('w'):
            movePad(scr, pad, 0, -1)

        elif ch == curses.KEY_DOWN or ch == ord('s'):
            movePad(scr, pad, 0, 1)

        elif ch == ord("q"):
            break

        scr.refresh()

        # Sleep until next round
        time.sleep(0.05)



if __name__ == "__main__":
    print(__doc__)
    print(main.__doc__)
    input("Press enter to begin playing...")
    curses.wrapper(main)
