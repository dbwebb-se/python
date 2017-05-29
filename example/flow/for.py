#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for i in range(10):
    print(i)


for i in range(10):
    number = i + 1
    if number > 5:
        print("Stor")
    else:
        print("Liten")


for _ in range(5):
    print("python är ett spännande programmeringsspråk")


for letter in "räksmörgås":
    if letter in "åäö":
        print(letter)
