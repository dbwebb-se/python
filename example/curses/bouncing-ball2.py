#!/usr/bin/env python3
"""
Evolving the bouncing ball to include other items
"""

import curses
from curses import KEY_RIGHT, KEY_LEFT


def main(screen):
    """
    Bounce a ball on a board and assign points for each bounce.
    """
    curses.curs_set(0)

    max_y, max_x = screen.getmaxyx()

    ball = "o"
    board = "_"*20
    board_x = max_x//2 - len(board)//2

    ball_y, ball_x = 3, 3
    vert_dir = 1
    hori_dir = 1

    delay = 15
    delayed = 0
    life = 3
    score = 0

    screen.timeout(0)

    while True:
        screen.clear()

        screen.addstr(0, 0, "Score: " + str(score))
        screen.addstr(1, 0, "Lives left: " + str(life))
        screen.addstr(ball_y, ball_x, ball)
        screen.addstr(max_y-1, board_x, board)
        
        q = screen.getch()

        # if possible, move paddle
        if q == KEY_LEFT and board_x > 0:
            board_x -= 1
        elif q == KEY_RIGHT and board_x < max_x-1-len(board):
            board_x += 1
        # quit
        elif q == ord("q"):
            #screen.clear()
            text = "GAME OVER!"
            screen.addstr(max_y//2, max_x//2-len(text)//2, text)
            screen.refresh()
            curses.napms(2500)
            break

        if delayed >= delay:
            # check where ball is and reverse dir if needed
            if ball_y == max_y-1 or ball_y == 0:
                vert_dir = -vert_dir # reverse top
            if ball_x == max_x-len(ball)-1 or ball_x == 0:
                hori_dir = -hori_dir # reverse
            if ball_y == max_y-2:
                if ball_x > board_x and ball_x < board_x+len(board):
                    vert_dir = -vert_dir # reverse top
                    score += 1
                    if score > 1 and score % 5 == 0 and len(board) > 8:
                        board = board[1:]
                    elif score > 1 and score % 5 == 0 and delay > 8:
                        delay -= 1
                    screen.refresh()
                # potential board bounce
            if ball_y == max_y-1:
                if ball_x < board_x or ball_x > board_x+len(board):
                    life -= 1
                    ball_y, ball_x = 3, 3
                    vert_dir, hori_dir = 1, 1
                    if life == 0:
                        #screen.clear()
                        text = "GAME OVER!"
                        screen.addstr(max_y//2, max_x//2-len(text)//2, text)
                        screen.refresh()
                        curses.napms(2500)
                        break
                elif ball_x > board_x and ball_x < board_x+len(board):
                    score += 1
                    if score > 1 and score % 5 == 0 and len(board) > 8:
                        board = board[1:]
                    elif score > 1 and score % 5 == 0 and delay > 8:
                        delay -= 1
                    screen.refresh()
            ball_x += hori_dir
            ball_y += vert_dir
            delayed = 0

        delayed += 1
        curses.napms(5)
    
    curses.endwin()

    print("Final score:", score)


if __name__ == "__main__":
    print(main.__doc__)
    curses.wrapper(main)
    
