#!/usr/bin/env python3
"""
Example code for the LEGB-rule and scopes
"""

x_one = "global"

def global_one():
    """Example 1"""
    print("x_one inside:", x_one)

global_one()
print("x_one outside:", x_one)
# Prints:
# x_one inside: global
# x_one outside: global



x_two = "global"

def global_two():
    """Example 2"""
    x_two = x_two * 2 #pylint: disable=used-before-assignment
    print(x_two)

global_two()
# Prints:
# UnboundLocalError: local variable 'x_two' referenced before assignment



def local_one():
    """Example 3"""
    y_three = "local" #pylint: disable=unused-variable

local_one()
print(y_three) #pylint: disable=undefined-variable
# Prints:
# NameError: name 'y_three' is not defined



def local_two():
    """Example 4"""
    y_four = "local"
    print(y_four)

local_two()
# Prints:
# local



x_five = "global "
y_five = "global"

def local_and_global_one():
    """Example 5"""
    global x_five
    y_five = "local"
    x_five = x_five * 2
    print("x_five inside:", x_five)
    print("y_five inside:", y_five)

local_and_global_one()
print("x_five outside:", x_five)
print("y_five outside:", y_five)
# skriver ut:
# x_five inside: global global
# y_five inside: local
# x_five outside: global global
# y_five outside: global



def outer():
    """Example 6"""
    x_six = "local"

    def inner():
        nonlocal x_six
        x_six = "nonlocal"
        print("inner:", x_six)

    inner()
    print("outer:", x_six)

outer()
# skriver ut:
# inner: nonlocal
# outer: nonlocal
