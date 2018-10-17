#!/usr/bin/env python3
"""
Write your code in this file. Fill out the defined functions with your solutions.
You are free to write additional functions and modules as you see fit.
"""
import analyze_functions_andreas as analyze_functions

def analyze_text():
    """
    Analyze myths.txt on sentences and gods
    """
    while True:
        choice = input("Enter s, g or q/quit: ")

        if choice == "s":
            analyze_functions.count_sentences()
        elif choice == "g":
            analyze_functions.count_Bgods()
        elif choice in ("q", "quit"):
            break
        else:
            print("Not an option!")

    return True

def verify_hex(hex_value):
    """
    Assignment 2
    """
    hex_numbers = "0123456789abcdef"
    if hex_value.startswith("#"):
        if len(hex_value) in (4, 7):
            for number in hex_value[1:]:
                if not number in hex_numbers:
                    return False
            return True
    return False



if __name__ == '__main__':
    analyze_text()
    # Should be True
    print(verify_hex("#fff"))
    print(verify_hex("#000"))
    print(verify_hex("#fc6c85"))
    print(verify_hex("#6495ed"))
    # Should be False
    print(verify_hex("fff"))
    print(verify_hex("#ffff"))
    print(verify_hex("fff#"))
    print(verify_hex("#FFFFFF"))
