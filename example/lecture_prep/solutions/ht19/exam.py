#!/usr/bin/env python3
"""
Write your code in this file. Fill out the defined functions with your solutions.
You are free to write additional functions and modules as you see fit.
"""
import analyze_functions

def analyze_text():
    """
    Assignment 1
    """
    while True:
        choice = input("Gör ett val: ")

        if choice in ("q", "quit"):
            break
        elif choice == "s":
            analyze_functions.sentences()
        elif choice == "g":
            analyze_functions.gods()
        else:
            print("Not an option!")

    return True

def verify_hex(hex_value):
    """
    Assignment 2
    Strängen börjar med en brädgård '#'.
    Strängen består sedan av 3 eller 6 hexadecimala siffror 0-f.
    Alla bokstäver ska vara små bokstäver.
    """
    valid_chars = "0123456789abcdef"
    if hex_value[0] == "#":
        if len(hex_value) == 4 or len(hex_value) == 7:
            for value in hex_value[1:]:
                if value not in valid_chars:
                    return False
            return True
    return False



if __name__ == '__main__':
    analyze_text()
    #print(verify_hex("#000000"))
