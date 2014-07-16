#!/usr/bin/env python3 
"""
Testing out the curses lib.

"""

#from curses import wrapper
import time
import curses
import random
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

def main(screen):
	"""
	Snake
	"""
	screen.clear()

	# Remove cursor
	curses.curs_set(0)
	# Don't wait for input
	screen.nodelay(1)

	# Set some colorpairs
	curses.start_color()
	# --------------------------------------------------------
	# ASSIGNMENT
	# Add more colorpairs for later use
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

	# Border
	screen.border()

	# Get the y,x of the window
	max_y, max_x = screen.getmaxyx()
	# Get the center of the window as tuple
	center = (max_y//2), (max_x//2)
	# Snake starting position
	x = center[1]
	y = center[0]

	# Direction as dictionary
	dirs = {"x": 1, "y": 0}

	# Snake
	snake_ch = "O"
	snake = [[y,x], [y,x-1], [y,x-2]]

	# Apple
	apple = [random.randint(1, max_y-2), random.randint(1, max_x-2)]
	apple_ch = "ö"

	# Game values
	score = 0

	# --------------------------------------------------------
	# ASSIGNMENT
	# Use a colorpair
	screen.addstr(snake[0][0], snake[0][1], snake_ch)

	# --------------------------------------------------------
	# ASSIGNMENT
	# Use a colorpair
	screen.addstr(apple[0], apple[1], apple_ch)

	screen.refresh()

	while True:
		# Add score text
		screen.addstr(0, 2, "Score : " + str(score) + " ")

		key = screen.getch()
		if key == ord("q"):
			text = "GAME OVER!"
			screen.addstr(max_y//2, max_x//2-len(text)//2, text)
			screen.refresh()
			curses.napms(2500)
			break
		# --------------------------------------------------------
		# ASSIGNMENT
		# Add elif's for handling arrow-keys for snake movement
		# Remember to:
		# 	Change the direction-values in dirs-dictionary depening on what key was pressed


		# Move
		x += dirs["x"]
		y += dirs["y"]

		# --------------------------------------------------------
		# ASSIGNMENT
		# Make sure the head of the snake is inside border
		# Remember to:
		# 	Count for the border
		# 	End game if hit border


		# --------------------------------------------------------
		# ASSIGNMENT
		# Insert new position of snake's head into the snake-list
		# Remember to:
		# 	Insert it first, not last


		# --------------------------------------------------------
		# ASSIGNMENT
		# Check if snake at itself
		# TIP: Check if the head at pos 0 in the snake-list can be found in the rest of the list
		# Remember to:
		# 	End game if ate self


		# --------------------------------------------------------
		# ASSIGNMENT
		# Check if snake's head ate apple
		# Remember to:
		# 	Get a new position for apple
		# 	Add the new apple to the screen
		# 	Add point to score for apple eaten

		# --------------------------------------------------------
		# ASSIGNMENT
		# If snake did not eat apple, pop the last position of the snake and remove the char at that positon
		# It will make the snake appear to move forward instead of just getting longer and longer


		# --------------------------------------------------------
		# ASSIGNMENT
		# Use a colorpair
		screen.addch(snake[0][0], snake[0][1], snake_ch)

		# Move snake every 0.1 sec (100ms)
		curses.napms(100)

	curses.endwin()
	print("Final score:", score)


if __name__ == "__main__":
	print(main.__doc__)
	curses.wrapper(main)
