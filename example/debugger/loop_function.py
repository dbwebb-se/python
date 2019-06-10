#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example script showing usage of while-loop for article
Villkor och loopar
"""
# import pdb
def print_apples(number_of_apples):
    """
    Print based on number of apples left
    """
    if number_of_apples > 10:
        print("Du har mer än 10 äpplen")
    elif number_of_apples <= 10 and number_of_apples > 5:
        # pdb.set_trace()
        print("Du blev snabbt mätt och åt bara upp några av dina äpplen")
    else:
        print("Du har nog varit hungrig och ätit upp dina äpplen")

while True:
    user_input = input("Skriv in antal äpplen (eller q för avslut): ")
    if user_input == "q":
        print("Du är nu klar med att äta äpplen.")
        print("Hej då!")
        break
    else:
        try:
            number_of_apples = int(user_input)
        except ValueError:
            pdb.set_trace()
            print("Oj! Du skrev inte in en siffra.")
            continue

        print_apples(number_of_apples)
