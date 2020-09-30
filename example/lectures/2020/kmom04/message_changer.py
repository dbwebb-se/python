"""
Assigment 2
"""
import string_modifier

def take_message():
    """
    Switch uppers and lowers in a string
    """
    msg = input("Enter a crasy case message: ")
    new_msg = ""
    for letter in msg:
        new_msg += string_modifier.case_switch(letter)
    print(new_msg)

if __name__ == "__main__":
    take_message()
