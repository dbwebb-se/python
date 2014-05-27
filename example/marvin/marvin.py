#!/usr/bin/python3

"""
Marvin with a simple menu to start up with.

"""

def menu():
    """
    Display the menu with options that Marvin can do.
    """
    print("1) State your name and meet Marvin.")
    print("q) Quit.")



def main():
    """
    This is the main method, I call it main by convention.
    """
    while True:
        menu()
        choice = input("--> ")
        
        if choice == "q":
            break
        else:
            print(choice)



if __name__ == "__main__":
        main()
