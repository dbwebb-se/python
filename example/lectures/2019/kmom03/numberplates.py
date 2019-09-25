"""
Checks validity of swedish numberplates
"""
def is_valid_numberplate(numberplate):
    """
    Checks validity
    """
    valid = True

    if len(numberplate) != 6:
        valid = False

    if valid:
        if not (numberplate[0:3].isupper() and numberplate[0:3].isalpha()):
            valid = False
        if valid:
            for letter in numberplate[3:]:
                if not letter.isdigit():
                    valid = False
                    break

    if valid:
        print("Nummerskylten är OK")
    else:
        print("Nummerskylten är inte OK")


def take_input():
    """
    Takes input and sends choice to validity function
    """
    while True:
        choice = input("Input numberplate or done for quit: ")

        if choice == "done":
            break
        else:
            is_valid_numberplate(choice)

take_input()
