#!/usr/bin/env python3
"""
Write your code in this file. Fill out the defined functions with your solutions.
You are free to write additional functions and modules as you see fit.
"""
import analyze_functions_solution as analyze_functions
import date_time_functions_solution as date_time_functions



def analyze_text():
    """
    Analyze a text file for different characters
    """
    while True:
        c = input("What to do? ")
        if c in ("s", "spaces"):
            print(analyze_functions.spaces())
        elif c in ("l", "letters"):
            print(analyze_functions.letters())
        elif c in ("c", "specials"):
            print(analyze_functions.specials())
        elif c in ("q", "quit"):
            break
        else:
            print("Not an option!")

    return True



def validate_mobile(number):
    """
    Validate mobile number
    """
    if len(number) == 13 and number[3] == "-" and number[7] == " " and number[10] == " ":
        if number[0:3] in ["070", "072", "073", "076", "079"]:
            n = number[4:].replace(" ", "")
            for c in n:
                if not c.isdigit():
                    return False
            return True

    return False



def verify_credit_card(number):
    """
    Verify credit card numbers
    """
    control = number[-1]
    sequence = [int(x) for x in list(number)[:-1]]
    for i, s_number in enumerate(sequence):
        if i % 2 == 0:
            temp = int(s_number) * 2
            if temp > 9:
                tmp = str(temp)
                temp = int(tmp[0]) + int(tmp[1])
            sequence[i] = temp
    tot = sum(sequence)
    tot *= 9
    return control == str(tot)[-1]



def find_difference(items, items2):
    """
    Find uniqe values between lists
    """
    result = check_dup(items, items2)
    result += check_dup(items2, items)

    return sorted(result)



def check_dup(items_, items2_):
    """
    check for duplicates in lists
    """
    result = {}
    for item in items_:
        is_dup = False
        for item2 in items2_:
            if item.lower() == item2.lower():
                is_dup = True
        if not is_dup:
            result[item] = item
    return list(result.keys())



def validate_date_time():
    """
    Find valid dates and times in text
    """
    while True:
        c = input("Enter a choice: ")
        if c in ("d", "date"):
            date_time_functions.find_dates()
        elif c in ("t", "time"):
            date_time_functions.find_times()
        elif c in ("q", "quit"):
            return True
        else:
            print("Not an option!")
    return True



if __name__ == '__main__':
    analyze_text()
    validate_mobile("")
    verify_credit_card("")
    find_difference([], [])
    validate_date_time()
