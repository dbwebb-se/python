#!/usr/bin/env python3
"""
Testing out some animation in curses
"""

import curses
import time

def main(screen):
    """
    Draw a ball that bounces off the sides
    """
    # Don't stop the while-loop while waiting for input
    screen.nodelay(1)

    # Get dimensions
    max_y, max_x = screen.getmaxyx()

    # The ball
    my_str = "O"

    # Starting position
    x, y = 0, 0
    # Directions
    vert, hori = 1, 1

    while True:
        screen.clear()
        # Draw the ball
        screen.addstr(y, x, my_str)
        # Move cursor out of the way
        screen.move(0, 0)
        screen.refresh()

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
        q = screen.getch()
        if q > -1:
            break


if __name__ == "__main__":
    print(main.__doc__)
    curses.wrapper(main)