#!/usr/bin/env python3
# -*- coding: utf-8 -*-

number = 2

while number < 20:
    print(number)
    number = number + number


mega_sum = 0

while True:
    user_input = input("Skriv in en siffra (eller q för avslut): ")
    if user_input == "q":
        print("MegaSum: " + str(mega_sum))
        break
    else:
        number = int(user_input)
        mega_sum += number
