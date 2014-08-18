#!/usr/bin/env python3
"""
Testing out the curses lib.

"""

#from curses import wrapper
import curses


def main(scr):
    """
    Draw a border around the screen.
    """
    # Clear the screen of any output
    scr.clear()

    # Get screen dimensions
    y1, x1 = scr.getmaxyx()
    y1 -= 1
    x1 -= 1

    y0, x0 = 0, 0
    # Get center position
    yc, xc = (y1-y0)//2, (x1-x0)//2

    # Draw a border
    scr.border()

    # Move cursor to center
    scr.move(yc, xc)

    # Refresh to draw out
    scr.refresh()

    # Main loop
    x = xc
    y = yc
    ch = 'o'
    while True:
        key = scr.getkey()
        if key == 'q':
            break
        elif key == 'KEY_UP':
            y -= 1
        elif key == 'KEY_DOWN':
            y += 1
        elif key == 'KEY_LEFT':
            x -= 1
        elif key == 'KEY_RIGHT':
            x += 1
        else:
            ch = key # change the char to draw to the inputed key

        # --------------------------------------------------------
        # ASSIGNMENT
        # Add code so that user can not move outside of the border
        #

        # As long as key was not spacebar - draw out the char at cursor
        if ch != ' ':
            scr.addstr(ch)

        # Move cursor to new position
        scr.move(y, x)

        # Refresh
        scr.refresh()


if __name__ == "__main__":
    print(main.__doc__)
    curses.wrapper(main)
