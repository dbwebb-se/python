#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A rough outline to a game of snake.

Steer using arrow-keys or keys "asdw".
"""

import curses
import time


def main(scr):
    """
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

    # The snake
    snake = {
        "representation": "O",
        "max-length": 5,
        "position": [(max_x//2, max_y//2)],
        "direction": (1, 0)
    }

    # Do until exit
    while True:

        # Get input from user and flush the input buffer
        ch = scr.getch()
        
        # Check if a key was pressed and update
        if ch == curses.KEY_LEFT or ch == ord('a'):
            snake["direction"] = (-1, 0)

        elif ch == curses.KEY_RIGHT or ch == ord('d'):
            snake["direction"] = (1, 0)

        elif ch == curses.KEY_UP or ch == ord('w'):
            snake["direction"] = (0, -1)

        elif ch == curses.KEY_DOWN or ch == ord('s'):
            snake["direction"] = (0, 1)

        elif ch == ord("q"):
            break

       # Move one step forward
        x, y = snake["position"][0]
        dx, dy = snake["direction"]
        snake["position"].insert(0, (x+dx, y+dy))

        # Keep its size and remove tha last item from the snake & screen
        if len(snake["position"]) >= snake["max-length"]:
            x, y = snake["position"].pop()
            scr.addstr(y, x, " ")

        # Draw the snake
        for x, y in snake["position"]:
            scr.addstr(y, x, snake["representation"])

        scr.refresh()
        
        # Sleep until next round
        time.sleep(0.1)



if __name__ == "__main__":
    print(__doc__)
    print(main.__doc__)
    input("Press enter to begin playing...")
    curses.wrapper(main)
