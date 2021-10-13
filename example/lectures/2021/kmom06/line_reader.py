"""
Reads specific lines from file
"""

def read_specific_lines_from_file(filename, number_of_lines):
    """
    Reads specified lines from file specified as first argument
    """
    with open(filename, "r") as fh:
        lines = fh.readlines()

        for line in lines[:number_of_lines]:
            print(line.rstrip())


if __name__ == "__main__":
    specified_lines = int(input("How many lines do you want to print: "))
    read_specific_lines_from_file("manifesto.txt", specified_lines)
