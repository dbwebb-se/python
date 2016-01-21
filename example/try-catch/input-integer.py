#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Show how exceptions and try catch can be used
to handle troubles when reading integer variabels
using input.

"""

print(__doc__)

msg1 = "The integer value is {value}."
msg2 = "The type of the variabel is {type}."

# Read as string
aValue = input("Enter a integer value: ")

aType = type(aValue)

print(msg1.format(value=aValue))
print(msg1.format(value=aType))



# Read as integer
while True:
    aValue = input("Enter a integer value: ")
    try:
        aValue = int(aValue)
    except Exception:
        print("FAIL: You did not enter a integer.")
        continue
    break

aType = type(aValue)

print(msg1.format(value=aValue))
print(msg1.format(value=aType))
