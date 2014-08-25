#!/usr/bin/env python3

import curses
import time

def main(screen):
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
        screen.move(0,0)

        screen.refresh()

        # Move x and y in the current directions
        x += hori
        y += vert

        # --------------------------------------------------------
        # ASSIGNMENT
        # Remove current if-statements and instead check if new x and y is at any edge
        # Bounce ball if it is (reverse vertical or horizontal direction depending on which edge)
        # Remember to:
        #   Subtract 1 on max because the first position is 0
        #   Count for the lenght of the ball in horizontal check
        if y == max_y:
            y = 0
        if x == max_x:
            x = 0

        # Animate only every 0.1 sec so that you can actually see the ball move
        time.sleep(0.1)

        # Allow for an exit-key - any key pressed
        q = screen.getch()
        if q > -1:
            break


if __name__ == "__main__":
    print(main.__doc__)
    curses.wrapper(main)