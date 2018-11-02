"""
Module for analyze functions
"""



def specials():
    """
    Find special characters
    """
    vowels_ = """,".:-'?"""
    text = read_file().lower().split("\n")
    max_specials = 0
    for para in text:
        counter = 0
        for c in para:
            if c in vowels_:
                counter += 1
        if counter > max_specials:
            max_specials = counter
    return max_specials



def letters():
    """
    Calc number of letters
    """
    text = read_file()
    counter = 0
    for c in text:
        if c.isalpha():
            counter += 1
    return counter



def spaces():
    """
    Calc number of spaces
    """
    text = read_file()
    counter = 0
    for c in text:
        if c == " ":
            counter += 1
    return counter



def read_file():
    """
    Read file
    """
    with open("value-of-time.txt", "r") as fh:
        return fh.read()
