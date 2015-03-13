#!/usr/bin/env python3
"""
Example of how to read the content of a file into a list
"""

def read_file(filename):
    """
    Read a single line file and split it to a list
    """
    # with - as for reading a file automatically closes it after reading is done
    with open(filename) as filehandle:
        line = filehandle.readline();

    # print the line read from the file
    print(line)

    # split the line into a list on the comma ","
    items_as_list = line.split(",")

    # print what the list looks like
    print(items_as_list)

    return items_as_list


def save_list(list, filename):
    """
    Save a list of items to file, comma-separated
    """
    # join the list into a string with a comma ","" between every item
    list_as_str = ",".join(list)

    # show what the string looks like after join
    print(list_as_str)

    # write the line to the file
    with open(filename, "w") as filehandle:
        filehandle.write(list_as_str)


def main():
    """
    Main function to carry out the work.
    """

    # read the file into list
    items = read_file("items.txt")

    # add item to the list
    items.append("cup")

    # print what the list looks like after change
    print(items)

    # save the file
    save_list(items, "items.txt")


if __name__ == "__main__":
    print(__doc__)
    main()
