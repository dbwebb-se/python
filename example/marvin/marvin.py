#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.

"""


def meImage():
    """
    Store my ascii image in a separat variabel as a raw string
    """
    return r"""
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


def menu():
    """
    Display the menu with the options that Marvin can do.
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(meImage()) 
    print("Hi, I'm Marvin. I know it all. What can I do you for?") 
    print("1) Present yourself to Marvin.")
    print("q) Quit.")


def myNameIs():
    """
    Read the users name and say hello to Marvin.
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")



def main():
    """
    This is the main method, I call it main by convention.
    Its an eternal loop, until q is pressed. 
    It should check the choice done by the user and call a appropriate 
    function.
    """
    while True:
        menu()
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            return
        
        elif choice == "1":
            myNameIs()
        
        else:
            print("That is not a valid choice. You can only choose from the menu.")          
            
        input("\nPress enter to continue...")



if __name__ == "__main__":
    main()
