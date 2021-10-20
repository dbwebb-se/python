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
        choice = input("Enter choice: ")
        if choice == "s":
            analyze_functions.count_sentences()
        elif choice == "g":
            analyze_functions.count_gods()
        elif choice in ("q", "quit"):
            break
        else:
            print("Not an option!")
    return True

def verify_hex(hex_value):
    """
    Strängen börjar med en brädgård '#'.
    Strängen består sedan av 3 eller 6 hexadecimala siffror 0-f.
    Alla bokstäver ska vara små bokstäver.
    """
    allowed_chars = "0123456789abcdef"
    verified = False
    if hex_value[0] == "#":
        if len(hex_value) in (4, 7):
            verified = True
            for char in hex_value[1:]:
                if char not in allowed_chars:
                    verified = False
                    break
    return verified



if __name__ == '__main__':
    analyze_text()
    # print(verify_hex("#ff0000"))
