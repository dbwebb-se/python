#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example to show how a multi dimensional array works in Python.
The "array" is implemented using lists of lists.
Press 's' to save the state to the file and press 'l' to load the 
state from the file. 
"""
# pylint: disable=consider-using-enumerate


filename = 'matrix.txt'



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



def saveMatrix(matrix):
    """
    Save the content of the matrix to a file. Do this by joining all items in the 
    list and create a string-representing the row and write that string to the file.
    Add a newline to each row. 
    """
    with open(filename, 'w') as f:
        for row in matrix:
            f.write("".join(row) + '\n')

    print(f"Saved the state to the file {filename}")



def loadMatrix(matrix):
    """
    Load the content of the matrix from a file. Do this by reading the lines from the file
    and splitting them into a list by characters. 
    Ignore the newline at each row. 
    """
    with open(filename, 'r') as f:

        # with \n
        #content = f.readlines()
        
        # without \n
        content = f.read().splitlines()

        # Update each row of the matrix and fill it by using the file content 
        # (may need som care when file and matrix size does not match)
        for y in range(0, len(matrix)):
            matrix[y] = list(content[y])

    print(f"Loaded the state from the file {filename}")



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

        elif posY == "s" or posX == "s":
            saveMatrix(matrix)
            continue

        elif posY == "l" or posX == "l":
            loadMatrix(matrix)
            continue

        #Place the character
        matrix[int(posY)][int(posX)] = char



if __name__ == "__main__":
    print(__doc__)
    input("Press enter to continue.")
    main()
