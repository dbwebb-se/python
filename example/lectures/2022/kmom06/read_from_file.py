"""
Reads from file
"""

def read_from_file(filename):
    """
    Reads from file specified as argument
    """
    # with opens the file, reads and closes the file with the statement is finished
    #with open(filename, "r") as filehandler: # read is default, add "r" to clarify
    #    print(filehandler.read()) # read(10), only the 10 first characters are read

    with open(filename, "r", encoding='utf8') as filehandler:
        content = filehandler.readlines()

    return content

if __name__ == "__main__":
    line_list = read_from_file("read_from.txt")
    print(line_list)
