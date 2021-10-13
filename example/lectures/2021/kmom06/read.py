"""
Reads from file
"""
def read_from_file(filename):
    """
    Reads from file specified as argument
    """
    with open(filename, "r") as fh:
        for line in fh.readlines():
            for letter in line:
                print(letter)

if __name__ == "__main__":
    read_from_file("read_from.txt")
