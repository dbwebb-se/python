#!/usr/bin/env python3 
"""
Testing out the curses lib.

"""

#from curses import wrapper
import time
import curses



def main(scr):
    """
    Draw a border around the screen.
    """
    scr.clear()

    # Get the x of the window
    x0 = 0
    x1 = curses.COLS - 1

    # Get the y of the window
    y0 = 0
    y1 = curses.LINES - 1

    # Get the center of the window
    yc = (y1 - y0) // 2
    xc = (x1 - x0) // 2

    for x in range(x0 + 1, x1):
        scr.addch(y0, x, '-')
        scr.addch(y1, x, '-')

    for y in range(y0 + 1, y1):
        scr.addch(y, x0, '|')
        scr.addch(y, x1, '|')

    scr.move(yc, xc);
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

        if y <= y0:
            y = y0 + 1
        elif y >= y1:
            y = y1 - 1
        if x <= x0:
            x = x0 + 1
        elif x >= x1:
            x = x1 - 1

        if ch != ' ':
            scr.addstr(ch)
        
        scr.move(y, x)
        scr.refresh()



if __name__ == "__main__":
        print(main.__doc__)
        curses.wrapper(main)


