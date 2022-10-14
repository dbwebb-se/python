"""
Reads specified lines from file
"""

def read_specified_lines_from_file(filename, number_of_lines):
    """
    Reads specified lines from file specified as first argument
    """
    with open(filename, "r") as fh:
        lines = fh.readlines()

        for line in lines[:number_of_lines]:
            print(line.rstrip()) # rstrip removes whitespaces to the right, such as 
            # space ' ', tab '\t', newline '\n' etc


if __name__ == "__main__":
    specified_lines = int(input("How many lines do you want to print: "))
    read_specified_lines_from_file("manifesto.txt", specified_lines)
