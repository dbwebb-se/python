#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example script showing usage of if-statements for article
Villkor och loopar
"""


number_of_apples = 13

if number_of_apples > 10:
    print("Du har mer än 10 äpplen")


number_of_apples = 9

if number_of_apples > 10:
    print("Du har mer än 10 äpplen")
else:
    print("Du har nog varit hungrig och ätit upp dina äpplen")


number_of_apples = 9

if number_of_apples > 10:
    print("Du har mer än 10 äpplen")
elif number_of_apples <= 10 and number_of_apples > 5:
    print("Du blev snabbt mätt och åt bara upp några av dina äpplen")
else:
    print("Du har nog varit hungrig och ätit upp dina äpplen")


type_of_fruit = "päron"
number_of_fruits = 13

if number_of_fruits > 10:
    if type_of_fruit == "äpple":
        print("Du har mer än 10 äpplen")
    else:
        print("Du har mer än 10 frukter")
