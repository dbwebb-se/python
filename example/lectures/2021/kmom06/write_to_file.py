"""
How to append to a file and delete lines from file
"""
def open_file():
    """
    read file content
    """
    try:
        # fd = open("data.txt", "r")
        with open("manifesto.txt", "r") as fd:
            return fd.read()
    except FileNotFoundError:
        print("You are missing the file")
    return None

def add_line():
    """
    Append new line to end of file
    """
    new_line = input("Enter a new line")
    write_to_file("\n" + new_line, "a")

def remove_line_from_file(content):
    """
    Remove a line from file content and then write new content to file again
    """
    print(content)
    rm_line = input("Enter line to remove: ")
    content.pop(int(rm_line))
    content = "\n".join(content)
    write_to_file(content, "w")
    

def write_to_file(content, mode):
    """
    Write content to file.
    Opens with the mode sent as argument, "w" or "a".
    """
    with open("manifesto.txt", mode) as fh:
        fh.write(content)

def menu():
    """
    Main menu for program
    """
    while True:
        inp = input("""Enter option:
1. Read replace
2. insert new line
3. remove line
""")
        if inp == "1":
            print(open_file())
        elif inp == "2":
            add_line()
        elif inp == "3":
            content = open_file()
            remove_line_from_file(content.split("\n"))
        else:
            exit()
 
if __name__ == "__main__":
    menu()
