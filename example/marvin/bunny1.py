#!/usr/bin/env python3

"""
Bunny with a menu to do stuff
"""

import random
import math

def menu():
    """
    Display the menu with options of what Bunny can do
    """
    print ("""
     _     _
    /_\\   /_\\
   ////  ////
  ////  ////       ____________________________
  \\\\\\\\_////       /                            \\
   \\     /       /   Hi, I'm Bunny.             \\
    \\O O/        \\    What can I do for you?    /
 ===/ ^ \\===      \\  __________________________/
    \\___/         /_/
    _/ \\_
  _//   \\\\_
 /__\\/_\\/__\\

    0. Quit
    1. Say hello
    2. Get age in seconds
    3. Get weight on the moon
    4. Get hours from minutes
    5. Convert celcius to fahrenheit
    6. Print a word lots of times
    7. Generate random number
    8. Print a number of random numbers
    9. Get average of numbers
    10. Get grade
    """)

# simple function and input, output
def hello():
    """
    Prompt user to input name and output a greeting
    """
    inpStr = input("What's your name?\n")
    print ("Hello", inpStr)


# calucations
def age_to_seconds():
    """
    Prompt user to input age and print out years in seconds
    Input is not filtered (missing use of try/except)
    """
    inp = input("How old are you?\n")
    years = int(inp)
    sec = years * 356 * 60 * 60
    print("You are over", sec, "seconds old!")


def moon_weight():
    """
    Prompt user to input weight and print out what that weight would be on the moon
    Input is not filtered (missing use of try/except)
    """
    inp = input("How much do you weigh?\n")
    weight = int(inp)
    moon_weight = weight/6
    print("You would weigh", moon_weight, "kg on the moon")


def get_hours():
    """
    Prompt user to input minutes and print them out in hours and minutes
    Input is not filtered (missing use of try/except)
    """
    inp = input("How many minutes?\n")
    minutes = int(inp)
    hours = minutes//60
    minutesLeft = minutes % 60
    print(hours, "hours and", minutesLeft, "minutes")


def cel_to_fahr():
    """
    Prompt user to input temperature in celcius and convert it to fahrenheit
    Input is not filtered (missing use of try/except)
    """
    inpStr = input("Enter Celcius temp: ")
    celFloat = float(inpStr)
    fahr = celFloat * (9/5) + 32
    print (celFloat, "C =", fahr, "F")


# word multiplyer
def print_word():
    """
    Prompt user to input a word and a number and print that word that many times
    Input is not filtered (missing use of try/except)
    """
    word = input("Enter word you want to repeat: ")
    times = input("Enter number of times to be repeated: ")
    times = int(times)
    print (word*times + " Watman!")


# random number in range
def random_integer():
    """
    Prompt user to enter a minimum and maximum number and randomate a number between those
    Input is not filtered (missing use of try/except)
    """
    print ("Please enter min and max numbers:")
    minStr = input("Min: ")
    maxStr = input("Max: ")
    minimum = int(minStr)
    maxinum = int(maxStr)
    randNr = random.randint(minimum, maxinum)
    print (randNr)


# loop
def print_random_numbers():
    """
    Prompt user to enter a minimum and maximum number and randomate 10 numbers between those
    Input is not filtered (missing use of try/except)
    """
    print ("Please enter min and max numbers:")
    minStr = input("Min: ")
    maxStr = input("Max: ")
    minimum = int(minStr)
    maxinum = int(maxStr)
    n = 0;
    nrs = ""
    while n < 10:
        nrs += str(random.randint(minimum, maxinum)) + ", "
        n += 1
    print (nrs)


# loop with break and try/except
def get_average():
    """
    Prompt user to enter numbers and print out the sum and average of those numbers
    Input is fileterd - has to be numeric
    """
    print ("Enter numbers to sum and average. Enter 'done' when you'd like to finish and get the average")
    n = 0
    sum_to_average = 0
    while True:
        line = input("> ")
        if line == "done":
            break
        try:
            sum_to_average += int(line)
            n += 1
        except:
            print ("Please enter a number")
    print ("Sum:", sum_to_average, ", average:", sum_to_average / n)


# loop with break and if-else
def get_grade():
    """
    Prompt the user to enter a maximum score and the user's own score. Print out the grade of that score.
    Input is filtered - has to be numeric
    """
    while True:
        try:
            inp = input("Enter maximum score: ")
            maxScore = int(inp)
            break;
        except:
            print("Please enter a numeric value")
    while True:
        try:
            inp = input("Enter your score: ")
            score = int(inp)
            break;
        except:
            print("Please enter a numeric value")
    #print(maxScore, score);
    percentage = score / maxScore
    if(percentage >= 0.9):
        grade = "A"
    elif(percentage >= 0.8):
        grade = "B"
    elif(percentage >= 0.7):
        grade = "C"
    elif(percentage >= 0.6):
        grade = "D"
    elif(percentage >= 0.5):
        grade = "E"
    elif(percentage < 0.5):
        grade = "F"
    print("You got an", grade)


# Main
def main():
    """
    This is the main method.
    """

    choice = None

    while choice != "0":
        menu()
        choice = input("--> ")
        
        if choice == "1":
            hello()
        elif choice == "2":
            age_to_seconds()
        elif choice == "3":
            moon_weight()
        elif choice == "4":
            get_hours()
        elif choice == "5":
            cel_to_fahr()
        elif choice == "6":
            print_word()
        elif choice == "7":
            random_integer()
        elif choice == "8":
            print_random_numbers()
        elif choice == "9":
            get_average()
        elif choice == "10":
            get_grade()
        elif choice == "0":
            print ("Quiting..")
            # break so that it doesn't prompt for enter
            break
        else:
            print ("Choice was invalid")
        # prompt for input before program continues and prints the menu again
        input("Press enter to continue...")


# run main
if __name__ == "__main__":
    main()
