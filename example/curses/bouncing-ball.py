#!/usr/bin/env python3 

import curses
import time



def main(screen):
	dims = screen.getmaxyx()
	screen.nodelay(1)

	myStr = "O"

	x, y = 0, 0
	vert = 1
	hori = 1
	while True:
		screen.clear()
		#screen.border()
		screen.addstr(y, x, myStr, curses.A_BOLD)
		screen.move(0,0)
		screen.refresh()
		x += hori
		y += vert
		if y == dims[0]-1 or y == 0:
			vert = -vert # reverse
		if x == dims[1]-len(myStr)-1 or x == 0:
			hori = -hori # reverse
		time.sleep(0.1)
		q = screen.getch()
		if q > -1:
		 	break


if __name__ == "__main__":
        print(main.__doc__)
        curses.wrapper(main)