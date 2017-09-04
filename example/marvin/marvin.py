#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

marvin_image = r"""
      ,     ,
     (\____/)
      (_oo_)
        (O)
      __||__    \/
   []/______\[] /
   / \______/ \/
  /    /__\
 /\   /____\
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
while True:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hi, I'm Marvin. I know it all. What can I do for you?")
    print("1) Present yourself to Marvin.")
    print("q) Quit.")

    choice = input("--> ")

    if choice == "q":
        print("Bye, bye - and welcome back anytime!")
        break

    elif choice == "1":
        name = input("What is your name? ")
        print("\nMarvin says:\n")
        print("Hello %s - your awesomeness!" % name)
        print("What can I do you for?!")

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
