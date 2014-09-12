#!/usr/bin/env python3
"""
Evolving the bouncing ball to include other things to hit
"""

import curses
from curses import KEY_RIGHT, KEY_LEFT


def main(screen):
    """
    Bounce a ball now becomes a simple breakout
    """
    curses.curs_set(0)

    max_y, max_x = screen.getmaxyx()

    x = 15

    ball = "o"
    board = "_"*x
    plate = "_"
    plate_y = 0, 1 # rows to have plates on
    plates = []

    
    for y in plate_y:
        count = 2
        while count < max_x-2:
            plates.append([y, count])
            count += len(plate)+1

    board_x = max_x//4 - len(board)//2

    ball_y, ball_x = 4, 2
    y_dir = 1
    x_dir = 1

    delay = 30
    delayed = 0
    life = 3
    score = 0

    screen.timeout(0)

    while True:
        screen.clear()

        text = "Score: " + str(score)
        screen.addstr(max_y-1, 0, text)
        screen.addstr(max_y-1, len(text)+5, "Lives left: " + str(life))
        screen.addstr(ball_y, ball_x, ball)
        for y, x in plates:
            screen.addstr(y, x, plate)
        screen.addstr(max_y-2, board_x, board)
        
        q = screen.getch()

        # if possible, move paddle
        if q == KEY_LEFT and board_x > 0:
            board_x += -1
        elif q == KEY_RIGHT and board_x < max_x-1-len(board):
            board_x += 1
        elif q == ord(" "):
            q = -1 # one (Pause/Resume)
            while q != ord(" "):
                q = screen.getch()
            continue
        # quit
        elif q == ord("q"):
            #screen.clear()
            text = "GAME OVER!"
            screen.addstr(max_y//2, max_x//2-len(text)//2, text)
            screen.refresh()
            curses.napms(2500)
            break

        if delayed >= delay:
            ball_x += x_dir
            ball_y += y_dir
            # check where ball is and reverse dir if needed
            next_y, next_x = ball_y+y_dir, ball_x
            if [next_y, next_x] in plates:
                # hit a plate
                plates.remove([next_y, next_x])
                score += 1
                if score > 1 and score % 2 == 0 and len(board) > 10:
                    board = board[1:]
                elif score > 1 and score % 2 == 0 and delay > 10:
                    delay -= 1
                y_dir = -y_dir # reverse
            elif [next_y, next_x+x_dir] in plates:
                plates.remove([next_y, next_x+x_dir])
                score += 1
                if score > 1 and score % 2 == 0 and len(board) > 10:
                    board = board[1:]
                elif score > 1 and score % 2 == 0 and delay > 10:
                    delay -= 1
                y_dir = -y_dir # reverse
            elif ball_y == max_y-2 or ball_y == 0:
                y_dir = -y_dir # reverse
            # side-bunce
            if ball_x == max_x-len(ball)-1 or ball_x == 0:
                x_dir = -x_dir # reverse
            # potential next board-bounce
            if ball_y == max_y-3:
                if ball_x+x_dir < board_x or ball_x+x_dir > board_x+len(board):
                    # ball will miss board
                    x_dir = -x_dir
                    life -= 1
                    if life == 0:
                        #screen.clear()
                        text = "GAME OVER!"
                        screen.addstr(max_y//2, max_x//2-len(text)//2, text)
                        screen.refresh()
                        curses.napms(2500)
                        break
                    y_dir = -y_dir
                    ball_x, ball_y = 4, 2
                if ball_x+x_dir > board_x and ball_x+x_dir < board_x+len(board):
                    # Ball hit board
                    y_dir = -y_dir

            if ball_x < 0:
                ball_x = 0
            elif ball_x >= max_x-len(ball)-1:
                ball_x = max_x-len(ball)-1
            
            if len(plates) == 0:
                text = "GAME OVER!"
                screen.addstr(max_y//2, max_x//2-len(text)//2, text)
                screen.refresh()
                curses.napms(2500)

            delayed = 0
            screen.refresh()

        delayed += 1
        curses.napms(3)
        
    
    curses.endwin()
    print("Final score:", score)
    print(plates)


if __name__ == "__main__":
    print(main.__doc__)
    curses.wrapper(main)
    
