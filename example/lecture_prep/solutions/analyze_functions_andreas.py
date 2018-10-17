# -*- coding: utf-8 -*-
"""
Module for analyze functions
"""


def count_sentences():
    """
    Find number of sentences in paragraphs
    """
    sents = []
    for para in read_file():
        sents.append(para.count("."))

    # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    print("\n".join([str(x) for x in sorted(sents, reverse=True)[:3]]))



def count_gods():
    """
    Find number of gods in paragraphs
    """
    gods = "Odin,Thor,Hödur,Baldur,Tyr,Heimdall,Vidar,Vali,Loki,Frigga,Freya,\
        Nanna,Iduna,Sif,Modi,Magni".split(",")
    count = []
    for para in read_file():
        count.append(sum([para.count(god) for god in gods]))

    # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    print("\n".join([str(x) for x in sorted(count, reverse=True)[:3]]))



def read_file():
    """
    Read file
    """
    with open("myths.txt", "r") as fh:
        for para in fh.read().split("\n\n"):
            yield para # https://docs.python.org/3/howto/functional.html#generators
