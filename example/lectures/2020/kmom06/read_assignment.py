"""
Read X number of lines from a file
"""

def print_lines(lines):
    """
    Iterate over file content and print X lines
    """
    nr = int(input("How many lines do you want to see? "))
    
    for line in lines[:nr]:
        print(line)
    print("------")

    counter = 0
    while counter < nr:
        print(lines[counter])
        counter += 1
    print("------")

    # Sämst sätt att lösa på
    for indx, line in enumerate(lines):
        if indx == nr:
            break
        print(line)


def read_file():
    """
    Read file content
    """
    try:
        with open("manifesto.txt", "r") as fd:
            print_lines(fd.read().split("\n"))
    except FileNotFoundError:
        print("You are missing the file")
        return


if __name__ == "__main__":
    read_file()
