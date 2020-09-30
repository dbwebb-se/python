import string_modifier

def take_message():
    msg = input("Enter a crasy case message: ")
    new_msg = ""
    for letter in msg:
        new_msg += string_modifier.case_switch(letter)
    print(new_msg)

if __name__ == "__main__":
    take_message()