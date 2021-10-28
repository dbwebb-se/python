#!/usr/bin/env python3
"""
Write your code in this file. Fill out the defined functions with your solutions.
You are free to write additional functions and modules as you see fit.
"""
import savingscentral_solution as sc
import stockbank_solution as ab

def count_elements(formula):
    """
    Assignment 1
    """
    elements = {}
    index = 0
    while index < len(formula):
        if formula[index].isupper():
            element = formula[index]
            try:
                if formula[index+1].islower():
                    element += formula[index+1]
                    index += 1
                index += 1
                if formula[index].isdigit():
                    try:
                        number =  int(formula[index:index+2])
                        index += 2
                    except (ValueError, IndexError):
                        number = int(formula[index])
                        index += 1
                else:
                    number = 1
                elements[element] = number
            except IndexError:
                number = 1
                elements[element] = 1
                index += 1
    return elements



def fotball_results(teams, matches):
    """
    Assignment 2
    """
    results = {}
    for team1, team2, score in matches:
        results[teams[team1]] = results.get(teams[team1], {
            "scores": 0,
            "points": 0,
            "games": 0 
        })
        results[teams[team2]] = results.get(teams[team2], {
            "scores": 0,
            "points": 0,
            "games": 0 
        })

        results[teams[team1]]["scores"] += int(score[0]) - int(score[2])
        results[teams[team2]]["scores"] += int(score[2]) - int(score[0])
        if int(score[0]) > int(score[2]):
            results[teams[team1]]["points"] += + 3
        elif int(score[0]) == int(score[2]):
            results[teams[team1]]["points"] += 1
            results[teams[team2]]["points"] += 1
        else:
            results[teams[team2]]["points"] += 3

        results[teams[team1]]["games"] += 1
        results[teams[team2]]["games"] += 1
    return results



def subset_zero():
    """
    Assignment 3
    """
    with open("numbers.txt") as fd:
        lists = fd.read().split("\n")
    for number_list in lists:
        int_numbers = []
        for number in number_list.split(", "):
            int_numbers.append(int(number))

        if 0 in int_numbers:
            print(int_numbers, True)
            continue
        found = False
        for number in int_numbers:
            if -number in int_numbers:
                found = True
                break
        print(int_numbers, found)



def jolly(numbers):
    """
    Assignment 4
    """
    first = True
    old_diff = 0
    res = ""
    is_jolly = True
    for index, number in enumerate(numbers[:-1]):
        diff = abs(number - numbers[index+1])
        res += " " + str(diff)
        if not first:
            if not old_diff - diff in (1, 0):
                is_jolly = False
        old_diff = diff
        first = False
    if is_jolly:
        res += " JOLLY"
    else:
        res += " NOT JOLLY"
    return res.lstrip()



def compare_banks():
    """
    Assignment 5
    """
    money_year = input("Enter money and year: ").split(",")
    try:
        sc_growth1 = sc.money_growth(int(money_year[0]), int(money_year[1]))
        ab_growth1 = ab.money_growth(int(money_year[0]), int(money_year[1]))
    except IndexError:
        sc_growth1 = sc.money_growth(int(money_year[0]))
        ab_growth1 = ab.money_growth(int(money_year[0]))
    except ValueError:
        return ()
    return (sc_growth1, ab_growth1)

if __name__ == '__main__':
    print(compare_banks())
    # print(compare_banks(10000, 5))
    # print(compare_banks(100, 20))
    # print(compare_banks(100, 0))
    # print(compare_banks(0, 10))

    # count_elements("")
    # subset_zero()
    # print(jolly([1, 4, 2, 3]))
    # print(jolly([8, 1, 6, -1, 8, 9, 5, 2, 7]))
    # print(jolly([5, 1, 4, 2, -1, 6]))
    # print(jolly([4, 19, 22, 24, 21]))
    # print(jolly([23, 19, 22, 24, 25]))
    # print(jolly([104, 52, 1, -50, 0])) # same
    # teams = ("Hammarby Dam", "Eskilstuna", "Kristianstad", "AIK Dam")
    # match_result = [(2,0,"1-2"),(1,0,"2-0"),(2,3,"1-1"),(3,1,"0-1"),(3,2,"1-3")]
    # print(fotball_results(teams, match_result))
    # print(fotball_results(("Hammarby Dam", "AIK Dam"), [(1, 0, "1-2"), (1, 0, "2-0")]))
