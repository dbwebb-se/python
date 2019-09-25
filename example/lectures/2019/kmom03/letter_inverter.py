"""
Inverts dem letters
"""

def invert(letter):
    """
    Change upper to lower and vice versa
    """
    if letter.isupper():
        return letter.lower()
    # else:
    return letter.upper()

def take_message():
    """
    Change upper/lower for a message
    """
    msg = input("Enter message: ")
    inverted_msg = ""
    for letter in msg:
        inverted_msg += invert(letter)
    print(inverted_msg)
take_message()
