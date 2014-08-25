#!/usr/bin/env python3 

import curses
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN


def main(screen):
    # Don't show cursor. Only works in Unix/Cygwin
    curses.curs_set(0)

    # Get dimensions
    max_y, max_x = screen.getmaxyx()

    # Ball values
    ball = "O"
    ball_y, ball_x = 4, 4
    vert_dir, hori_dir = 1, 1

    # Board values
    board = "_"*15
    board_x = max_x//2 - len(board)//2

    # Animation values
    delay = 15
    delayed = 0

    # Game values
    life = 3
    score = 0

    screen.timeout(0)

    while True:
        screen.clear()

        # Print game values
        screen.addstr(0,0, "Score: " + str(score))
        screen.addstr(1,0, "Lives left: " + str(life))
        # Print ball and board
        screen.addstr(ball_y, ball_x, ball)
        screen.addstr(max_y-1, board_x, board)
        
        # Allow for input
        q = screen.getch()

        # --------------------------------------------------------
        # ASSIGNMENT
        # If possible, move board
        # Remember to:
        #   Not move if board is at min or max positions
        #   Count for the lenght of the board at max
        #   Use KEY_LEFT and KEY_RIGHT to check which key was pressed


        # Quit
        if q == ord("q"):
            # Print text and wait before ending program
            text = "GAME OVER!"
            screen.addstr(max_y//2, max_x//2-len(text)//2, text)
            screen.refresh()
            curses.napms(2500)
            break

        # Only check ball status every full delay so that ball and board can move independet of eachother
        if delayed >= delay:
            # Check where ball is and reverse dir if needed
            if ball_y == max_y-1 or ball_y == 0:
                vert_dir = -vert_dir # reverse vertical
            if ball_x == max_x-len(ball)-1 or ball_x == 0:
                hori_dir = -hori_dir # reverse horizontal


            # --------------------------------------------------------
            # ASSIGNMENT
            # Check if ball is at board
            # Remember to:
            #   Count for the lenght of the board
            #   Reverse direction if ball hit board
            #   Give 1 point if ball hit board


            # --------------------------------------------------------
            # ASSIGNMENT
            # Check if ball is past board
            # Remember to:
            #   Count for the lenght of the board
            #   Rest ball position and direction to starting values if it was past board
            #   Withdraw a life
            #   End game if out of lives - tip: use the same code as in the quit-key-if


            # Move ball
            ball_x += hori_dir
            ball_y += vert_dir
            # Reset delay
            delayed = 0

        delayed += 1
        curses.napms(5)
    
    curses.endwin()

    print("Final score:", score)


if __name__ == "__main__":
    print(main.__doc__)
    curses.wrapper(main)