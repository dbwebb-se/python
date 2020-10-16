"""
Read format strings from a file and inject words
"""
def read_file(fd):
    """
    Itterate over file content and inject new words
    """
    for line in fd:
        print(line)
        word = input("enter new word: ")
        print(line.format(word))


def open_file():
    """
    Read file content
    """
    try:
        # fd = open("data.txt", "r")
        with open("data.txt", "r") as fd:
            read_file(fd)
    except FileNotFoundError:
        print("You are missing the file")
        return


if __name__ == "__main__":
    open_file()
