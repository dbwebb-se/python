#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Some various ways of saying Hello World in Python
Execute as cgi-skript and send a correct HTTP header.

"""

# Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()    



# Define a function
def hello():
    """
    Print out Hello World in a function.
    """
    print("Hello World in a function.")



# Send the HTTP header
print("Content-Type: text/plain;charset=utf-8")
#print("Content-Type: text/html;charset=utf-8")
print("")



# Here comes the content of the webpage 

# Call a function that prints out Hello World
hello()

# Print out Hello World
print("Just saying Hello World")

# Assign the string Hello World to a variable and print it out
#str = "Hello World in a variable"
#print(str)
str1 = "Hello World in a variable"
print(str1)
