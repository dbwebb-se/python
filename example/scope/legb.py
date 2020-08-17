#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example code for the LEGB-rule and scopes
"""

example_one_x = "global"

def example_one():
    """Exaple 1"""
    print("x inside:", example_one_x)

example_one()
print("x outside:", example_one_x)
# skriver ut:
# x inside: global
# x outside: global



# example_two_x = "global"

# def example_two():
#     """Exaple 2"""
#     example_two_x = example_two_x * 2
#     print(x)

# example_two()
# # skriver ut:
# # UnboundLocalError: local variable 'example_two_x' referenced before assignment



# def example_three():
#     """Exaple 3"""
#     example_three_y = "local"

# example_three()
# print(example_three_y)
# # skriver ut:
# # NameError: name 'example_three_y' is not defined



def example_four():
    """Exaple 4"""
    example_four_y = "local"
    print(example_four_y)

example_four()
# skriver ut:
# local



example_five_y = "global"

def example_five():
    """Exaple 5"""
    example_five_y = "local"
    print("y local:", example_five_y)

example_five()
print("y global:", example_five_y)
# skriver ut:
# y local: local
# y global: global



example_six_x = "global"

def example_six():
    """Exaple 5"""
    global example_six_x
    example_six_x = example_six_x * 2
    print("x inside:", example_six_x)

example_six()
print("x outside:", example_six_x)
# skriver ut:
# x inside: globalglobal
# x outside: globalglobal



def outer():
    """Example 7 has local scope acts as an enclosed scope for inner()"""
    x = "local"

    def inner():
        """Example 7 has local scope"""
        nonlocal x
        x = "nonlocal"
        print("x inner:", x)

    inner()
    print("x outer:", x)

outer()
# skriver ut:
# x inner: nonlocal
# x outer: nonlocal
