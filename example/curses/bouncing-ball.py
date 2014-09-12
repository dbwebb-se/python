#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testing out some animation in curses
"""

import curses
import time


def main(scr):
    """
    Draw a ball that bounces and changes direction when hitting the sides.

    Press any key to quit.
    """

    # Don't stop the while-loop while waiting for input
    scr.nodelay(1)

    # Get dimensions
    max_y, max_x = scr.getmaxyx()

    # The ball
    my_str = "O"

    # Draw a border
    scr.border()

    # Refresh to draw out
    scr.refresh()

    # Starting position
    x, y = 0, 0
    # Directions
    vert, hori = 1, 1

    while True:
        #scr.clear()
        
        # Draw the ball
        scr.addstr(y, x, my_str)
        
        # Move cursor out of the way
        scr.move(0, 0)
        scr.refresh()

        # Move x and y in the current directions
        x += hori
        y += vert

        # Check if new x and y is at any edge and bounce it if it is
        if y == max_y-1 or y == 0: # top and bottom
            vert = -vert # reverse
        if x == max_x-len(my_str)-1 or x == 0: # left and right
            hori = -hori # reverse

        # Animate only every 0.1 sec so that you can acutally see the ball move
        time.sleep(0.1)

        # Allow for an exit-key - any key pressed
        q = scr.getch()
        if q > -1:
            break



if __name__ == "__main__":
    print(__doc__)
    print(main.__doc__)
    input("Press enter to begin playing...")
    curses.wrapper(main)
