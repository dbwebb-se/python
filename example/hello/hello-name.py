#!/usr/bin/env python3

"""
Some various ways of saying Hello World in Python.
"""

# Print out Hello World
print("Just saying Hello World")

# Assign the string Hello World to a variable and print it out
str1 = "Hello World in a variable"
print(str1)

# Combine two strings and print them out
str2 = "Hello World!"
str3 = "Its a nice day today!"
print(str2 + " " + str3)

# Combine string and values
a = 40
b = 2
c = a + b
str4 = "Summan är " + str(c) + "."
print(str2 + " " + str4)

# Print out my name
name = "Mikael mos"
print("Mitt namn är " + name)

# Print out ASCII art
# Use prefix r for a raw string avoiding validation
marvin = r"""
       ,     ,
      (\____/)
       (_oo_)
         (O)
       __||__    \)
    []/______\[] /
    / \______/ \/
   /    /__\ 
  (\   /____\ 
"""
print(marvin)

marvin1 = r"""
                           (_)      
 _ __ ___   __ _ _ ____   ___ _ __  
| '_ ` _ \ / _` | '__\ \ / / | '_ \ 
| | | | | | (_| | |   \ V /| | | | |
|_| |_| |_|\__,_|_|    \_/ |_|_| |_|
"""
print(marvin1)
