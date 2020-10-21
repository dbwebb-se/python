#!/usr/bin/env python3
"""
Write your code in this file. Fill out the defined functions with your solutions.
You are free to write additional functions and modules as you see fit.
"""
import analyze_functions

def analyze_text():
    """
    Assignment 1 updated
    """
    while True:
        inp = input()
        if inp == "q":
            break
        elif inp == "v":
            print(analyze_functions.vowels())
        elif inp == "p":
            print(analyze_functions.periods())
        elif inp == "u":
            print(analyze_functions.uppers())
        else:
            print("Not an option!")
        input("...")
    return True

def validate_email(email):
    """
    Assignment 2 updated
    """
    allowed_chars = "abcdefghijklmnopqrstuvwxyz._-@0123456789"
    for i in email:
        if i not in allowed_chars:
            return False
    if email.count("@") == 1 and email.islower():
        first, end = email.split("@")
        if end.count(".") >= 1 and first:
            for i in end.split("."):
                if len(i) < 1:
                    return False
            if 1 < len(end.split(".")[-1]) < 4:
                return True
    return False

def list_median(values):
    """
    Assignment 3 updated
    """
    sorted_values = sorted(values)
    length = len(sorted_values)
    if length % 2 == 0:
        return round((sorted_values[length//2-1] + sorted_values[length//2]) / 2, 1)

    return sorted_values[(length-1)//2]

def find_duplicates(values):
    """
    Assignment 4 updated
    """
    counter = {}
    for v in values:
        if v.lower() in counter:
            counter[v.lower()] += 1
        else:
            counter[v.lower()] = 0
    dups = []
    for k, v in counter.items():
        if v > 0:
            dups.append(k)
    return sorted(dups)

def types(items):
    """
    Assignment 5 updated
    """
    result = []
    for i in items:
        if isinstance(i, int):
            i_mall = "The square of {} is {}."
            result.append(i_mall.format(i, i*i))
        elif isinstance(i, str):
            s_mall = "The secret word is {}."
            result.append(s_mall.format(i))
        elif isinstance(i, list):
            l_mall = "The list contains {}."
            result.append(l_mall.format(", ".join(i)))
        else:
            pass
    return " ".join(result)

if __name__ == '__main__':
    analyze_text()
    list_median([])
    find_duplicates([])
    types([])
    validate_email("")
