#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example script showing usage of for-loop for article
Villkor och loopar
"""

for i in range(10):
    print(i)


for number_of_apples in range(13):
    if number_of_apples > 10:
        print("Du har mer än 10 äpplen")
    elif number_of_apples <= 10 and number_of_apples > 5:
        print("Du blev snabbt mätt och åt bara upp några av dina äpplen")
    else:
        print("Du har nog varit hungrig och ätit upp dina äpplen")


for _ in range(5):
    print("python är ett spännande programmeringsspråk")


for letter in "räksmörgås":
    if letter in "åäö":
        print(letter)
