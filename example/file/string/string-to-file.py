#!/usr/bin/env python3
"""
Example of how to read and modify the content of a file
"""

# the name of the file
filename = "items.txt"

def menu():
    """
    Print available choices and return input
    """
    print(
        """
1. Show file content
2. Add item, append
3. Replace content
4. Remove an item
        """
        )
    return int(input("Choice: "))



def choice(inp):
    """
    Check which action was chosen
    """
    if inp == 1:
        print(readfile())
    elif inp == 2:
        write_to_file("\n" + input("Item to add: "), "a")
    elif inp == 3:
        replace_content()
    elif inp == 4:
        remove_item()
    else:
        exit()



def readfile():
    """
    Read string from file
    """
    # with - as for reading a file automatically closes it after reading is done
    with open(filename) as filehandle:
        content = filehandle.read()
    return content



def write_to_file(content, mode):
    """
    Write string to file
    """
    # open file with "w" to clear file from content and write new string to it
    with open(filename, mode) as filehandle:
        filehandle.write(content)



def replace_content():
    """
    Replace content of a file with new items
    """
    item = ""
    result = ""
    while item != "q":
        result += item + "\n"
        item = input("Item to add: ")
    write_to_file(result.strip(), "w") # strip(), remove leading or trailing newlines 



def remove_item():
    """
    Remove an item from the file
    """
    content = readfile()
    remove = input("What item should be removed: ")

    if remove in content: # check if item to remove exists
        if content.index(remove) == 0: # if the item is the first line in the file
            modified_content = content.replace(remove, "")
        else:
            modified_content = content.replace("\n" + remove, "")
        write_to_file(modified_content.strip(), "w")



if __name__ == "__main__":
    while(True):
        choice(menu())
