#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Work with lists to create a tic tac toe.
The program has limited checks on dealing with errors.
You could add code to check for a winner or tie game.
Or you could add som intelligence to the computer move.
"""

def printGame(board):
    """
    Print out the current game board.
    """
    print("-------        ")
    print("|{}|{}|{}| (1,2,3)".format(board[0], board[1], board[2]))
    print("|{}|{}|{}| (4,5,6)".format(board[3], board[4], board[5]))
    print("|{}|{}|{}| (7,8,9)".format(board[6], board[7], board[8]))
    print("-------        ")



def isInt(s):
    """
    Check that a string can be converted to a integer.
    """
    try:
        int(s)
        return True
    except ValueError:
        return False



def place(board, what, where):
    """
    Place a marker on the board.
    """
    board[where] = what



def placeComputer(board):
    """
    Place a marker on the board.
    """
    for position, value in enumerate(board):
        if value == " ":
            return position

    return False



def checkIfWinnerOrTie(board):
    """
    Check if there is a winner or if there is a tie game.
    """
    # pylint: disable=unused-argument
    print("(Checking for winner or tie is not yet implemented)")



def main():
    """
    Play a game of Tic Tac Toe.
    """

    # Create a list of nine spaces
    board = [" "] * 9

    print("Play against the computer.")
    print("You start, you are X. Computer is O.")
    print("Three in a row wins.")

    while 1:

        printGame(board)

        position = input("Enter position (1-9) to place you X (or q for quit): ")

        if position == "q":
            break

        elif isInt(position):
            # User move
            place(board, "X", int(position) - 1)
            
            # Computer move
            computerPos = placeComputer(board)
            if computerPos is not False:
                place(board, "O", computerPos)
                print("Computer moved to {}.".format(computerPos))

        if checkIfWinnerOrTie(board) is True:
            break


if __name__ == "__main__":
    print(__doc__)
    input("Press enter to continue.")
    main()
