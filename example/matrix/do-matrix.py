#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example to show how a multi dimensional array works in Python.
The "array" is implemented using lists. 
"""



print(__doc__)
input("Press enter to continue.")



def createMatrix(y, x, filler):
    """
    Create a two-dimensional array and return it. 
    """
    return [[filler for _ in range(x)] for _ in range(y)]



def printMatrix(matrix):
    """
    Print the content of the matrix. 
    """
    for row in matrix:
        print("".join(row))



def main():
    """
    Main function to carry out the work.
    """

    print("Enter the size of the matrix.")
    y = int(input("y: "))
    x = int(input("x: "))

    matrix = createMatrix(y, x, "-")

    counter = 0
    while 1:

        printMatrix(matrix)

        # Swap between X and O
        if counter % 2:
            char = "X"
        else:
            char = "O"

        counter += 1

        # Get a position to place the character
        posY = input("Enter a row: ")
        posX = input("Enter a column (or q for quit): ")

        if posY == "q" or posX == "q":
            break

        #Place the character
        matrix[int(posY)][int(posX)] = char



if __name__ == "__main__":
    main()
