#!/usr/bin/env python3 
"""
Testing out the curses lib.

"""

#from curses import wrapper
import curses
import random
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

def main(screen):
    """
    Snake

    Press 'q' to quit the game.
    """
    screen.clear()

    curses.curs_set(0)

    screen.nodelay(1)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Get the y,x of the window
    dims = screen.getmaxyx()

    # Get the center of the window
    center = (dims[0]//2), (dims[1]//2)

    screen.border()

    # Main loop
    x = center[1]
    y = center[0]

    dirs = {"x": 1, "y": 0}

    #screen.move(0, 0);
    screen.refresh()

    snake = [[y, x], [y, x-1], [y, x-2]]

    apple = [random.randint(1, dims[0]-2), random.randint(1, dims[1]-2)]
    appleCh = "ö"

    screen.addstr(apple[0], apple[1], appleCh, curses.color_pair(1))

    ch = "O"

    screen.addstr(snake[0][0], snake[0][1], ch, curses.color_pair(2))

    score = 0

    while True:
        screen.border()
        screen.addstr(0, 2, "Score : " + str(score) + " ")
        key = screen.getch()
        if key == ord("q"):
            #screen.clear()
            text = "GAME OVER!"
            screen.addstr(dims[0]//2, dims[1]//2-len(text)//2, text)
            screen.refresh()
            curses.napms(2500)
            break
        elif key == KEY_UP:
            dirs["y"] = -1
            dirs["x"] = 0
        elif key == KEY_DOWN:
            dirs["y"] = 1
            dirs["x"] = 0
        elif key == KEY_LEFT:
            dirs["x"] = -1
            dirs["y"] = 0
        elif key == KEY_RIGHT:
            dirs["x"] = 1
            dirs["y"] = 0

        x += dirs["x"]
        y += dirs["y"]

        # head of snake
        if y <= 0:
            y = 1
        elif y >= dims[0]-1:
            y = dims[0] - 2
        if x <= 0:
            x = 1
        elif x >= dims[1]-1:
            x = dims[1] - 2

        snake.insert(0, [y, x])

        if snake[0] in snake[1:]:
            #screen.clear()
            text = "GAME OVER!"
            screen.addstr(dims[0]//2, dims[1]//2-len(text)//2, text)
            screen.refresh()
            curses.napms(2500)
            break

        if snake[0] == apple:
            score += 1
            while apple in snake:
                apple = [random.randint(2, dims[0]-3), random.randint(2, dims[1]-3)]
            screen.addstr(apple[0], apple[1], appleCh, curses.color_pair(1))
        else:
            last = snake.pop()
            screen.addch(last[0], last[1], " ", curses.color_pair(2))

        screen.addch(snake[0][0], snake[0][1], ch, curses.color_pair(2))

        #time.sleep(0.1)
        nap_time = 100 - len(snake)//2
        curses.napms(nap_time)

    curses.endwin()
    print("Final score:", score)


if __name__ == "__main__":
    print(__doc__)
    print(main.__doc__)
    input("Press enter to begin playing...")
    curses.wrapper(main)
