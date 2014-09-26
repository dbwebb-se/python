#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testing out some animation in curses with a bouncing ball.
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

    # Draw a border
    scr.border()

    # Make cursor invisible
    curses.curs_set(0)

    # Get dimensions
    max_y, max_x = scr.getmaxyx()

    # The ball
    my_str = "O"

    # Starting position
    x, y = 0, 0

    # Directions
    vert, hori = 1, 1

    # Do until exit
    while True:

        # Move x and y in the current directions
        x += hori
        y += vert

        # Check if new x and y is at any edge and bounce it if it is
        # top and bottom
        if y == max_y - 1 or y == 0: 
            vert = -vert # reverse
        
        # left and right
        if x == max_x - len(my_str) or x == 0: 
            hori = -hori # reverse

        # Draw the ball
        scr.addstr(y, x, my_str)
        scr.refresh()
        
        # Allow for an exit-key - any key pressed
        q = scr.getch()
        if q > -1:
            break

        # Sleep until next round
        time.sleep(0.05)



if __name__ == "__main__":
    print(__doc__)
    print(main.__doc__)
    input("Press enter to begin playing...")
    curses.wrapper(main)
