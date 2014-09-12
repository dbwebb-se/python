#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testing out the curses lib.
"""

import curses


def main(scr):
    """
    Draw a border around the screen, move around using the cursor and leave a mark
    of the latest pressed character on the keyboard.

    Perhaps you could make a nice painting using asciart? 

    Quit using 'q'.
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
            ch = key

        # Draw out the char at cursor positino
        scr.addstr(ch)
        
        # Move cursor to new position
        scr.move(y, x)

        # Redraw all items on the screen
        scr.refresh()



if __name__ == "__main__":
    print(__doc__)
    print(main.__doc__)
    input("Press enter to begin playing...")
    curses.wrapper(main)
