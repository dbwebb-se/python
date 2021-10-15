"""
Further development of read.py..
Now can add new lines to file and delete
"""
def read_file(content):
    """
    itterate over file content
    """
    for line in content:
        print(line)
        word = input("enter new word: ")
        print(line.format(word))



def open_file():
    """
    read file content
    """
    try:
        # fd = open("data.txt", "r")
        with open("data.txt", "r") as fd:
            return fd.read()
    except FileNotFoundError:
        print("You are missing the file")
    return None



def add_line():
    """
    add new line to file
    """
    new_line = input("Enter new line: ")
    write_to_file("\n" + new_line, "a")



def write_to_file(content, mode):
    """
    write content to file
    """
    with open("data.txt", mode) as fd:
        fd.write(content)



def remove_line_from_file(content):
    """
    Remove a line from file
    """
    print(content)
    rm_line = input("Enter line number to remove: ")
    content.pop(int(rm_line))
    content = "\n".join(content)
    write_to_file(content, "w")



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
            content = open_file()
            read_file(content.split("\n"))
        elif inp == "2":
            add_line()
        elif inp == "3":
            content = open_file().split("\n")
            remove_line_from_file(content)
        else:
            exit()

if __name__ == "__main__":
    menu()
