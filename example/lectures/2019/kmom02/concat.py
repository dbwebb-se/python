"""
Emil's stupid error, where he said to students
that they should use isinstace() but solved with
try-except
"""

long_string = ""
while True:
    choice = input("Skriv in en sträng eller siffra: ")

    try:
        number_choice = int(choice)
        for _ in range(number_choice):
            print(long_string)
        long_string = ""
    except ValueError:
        long_string += choice
