#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testing out the curses lib.
"""

import curses

def debug(msg):
    """
    Ease debugging with curses by writing a message to file.
    """

    with open("debug.txt", "a") as f:
        f.write(msg + "\n")



def dump(scr, startX, startY, endX, endY):
    """
    Dump content of part of screen, do not output empty content.
    """

    with open("output.txt", "w") as f:
        for y in range(startY, endY):
            for x in range(startX, endX):

                # Get the character from screen
                ch = scr.inch(y, x)
                debug(str(x) + " - " + str(y) + ": " + str(ch))

                # Output only if not space
                if ch != 32:
                    ch = chr(ch & 0x00ff)
                    f.write(ch)



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
        elif key == 'o':
            dump(scr, 1, 1, x1, y1)
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
