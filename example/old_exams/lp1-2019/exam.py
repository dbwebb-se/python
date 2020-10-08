#!/usr/bin/env python3
"""
Write your code in this file. Fill out the defined functions with your solutions.
You are free to write additional functions and modules as you see fit.
"""

def find_replace():
    """
    Assignment 1
    """
    with open("manifesto.txt", "r") as fh:
        text = fh.read()
    find = input("Enter word to find: ")
    replace = input("Enter word to replace with: ")
    rows = text.split("\n")
    text_list = []
    for row in rows:
        row_words = row.split(" ")
        for index, word in enumerate(row_words):
            if word.strip(",.!\n") == find:
                if len(word) != len(word.strip(",.!")):
                    replace = replace + word[-1]
                row_words[index] = replace
        text_list.append(" ".join(row_words))
    with open("output.txt", "w") as fh:
        fh.write("\n".join(text_list))

def count_animals(animals):
    """
    Assignment 2
    """
    # import pdb; pdb.set_trace()
    result = ""
    for animal in sorted(animals):
        names = animals[animal]
        if isinstance(names, str):
            result += "1 " + animal + ": " + names + "\n"
        else:
            numbers = len(names)
            result += str(numbers) + " " + animal + ": " + ", ".join(sorted(names)) + "\n"

    return result.strip()


def validate_isbn(numbers):
    """
    Assignment 3
    """

    if len(numbers) == 13 and numbers.isdigit():
        mult_sum = 0
        for index, str_number in enumerate(numbers[:-1]):
            number = int(str_number)
            if index % 2:
                mult_sum += number * 3
            else:
                mult_sum += number
        check = 0
        if mult_sum % 10 != 0:
            check = 10 - (mult_sum % 10)

        return int(numbers[-1]) == check


    return False

def decide_winners(matches):
    """
    Assignment 4
    """
    result = []
    for match in matches:
        match_result = []
        for game in match:
            score = game.split("-")
            if int(score[0]) > int(score[1]):
                match_result.append(0)
            else:
                match_result.append(1)
        if match_result.count(0) > match_result.count(1):
            result.append("player1")
        else:
            result.append("player2")
    return result

def validate_bookings(bookings):
    """
    Assignment 5
    """
    for index, slot in enumerate(bookings):
        date = slot["date"]
        time = slot["time"].split("-")

        for other_index, other_slot in enumerate(bookings):
            if index == other_index:
                continue
            other_date = other_slot["date"]
            other_time = other_slot["time"].split("-")

            if date != other_date:
                continue
            if int(time[0]) <= int(other_time[0]) and int(time[1]) >= int(other_time[1]):
                return False

    return True

if __name__ == '__main__':
    find_replace()
    # print(count_animals({
    #     "ko": ["Mamma Mu", "Kalvin"],
    #     "gris": "Babe",
    #     "tupp": "Jussi",
    #     "höna": ["Juhani", "Aapo", "Tuomas", "Simeoni", "Timo", "Lauri", "Eero"]
    # }))
    # print(validate_isbn("9781617294136"))
    # print(decide_winners([["11-2", "5-11", "6-11",], ["11-3", "11-5",]]))
    # print(validate_bookings([
    #     {
    #         "date": "2019-10-28",
    #         "time": "10-12",
    #         "course": "DV1531"
    #     },
    #     {
    #         "date": "2019-10-28",
    #         "time": "9-10",
    #         "course": "PA1439"
    #     }
    # ]))
