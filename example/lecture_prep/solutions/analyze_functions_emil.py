# -*- coding: utf-8 -*-
"""
Module for analyze functions
"""

def count_sentences():
    """
    Find number of sentences in paragraphs
    """
    myths_list = read_file()
    top_score = []

    for myth in myths_list:
        top_score.append(myth.split(".") - 1)

    top_three = sorted(top_score, reverse=True)[:3]
    for top in top_three:
        print(top)

def count_gods():
    """
    Find number of gods in paragraphs
    """
    gods = [
        "Odin",
        "Thor",
        "Hödur",
        "Baldur",
        "Tyr",
        "Heimdall",
        "Vidar",
        "Vali",
        "Loki",
        "Frigga",
        "Freya",
        "Nanna",
        "Iduna",
        "Sif",
        "Modi",
        "Magni"
    ]
    
    myths_list = read_file()
    top_score = []
    for myth in myths_list:
        counter = 0
        for word in myth.split(" "):
            word = word.strip(".").strip(",").strip(";")
            if word in gods:
                counter += 1

        top_score.append(counter)

    top_three = sorted(top_score, reverse=True)[:3]
    for top in top_three:
        print(top)


def read_file():
    """
    Read file
    """
    with open("myths.txt", "r") as fh:
        myths = fh.read()
        return myths.split("\n\n")
