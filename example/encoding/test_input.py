#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Originated from a forumpost:
http://dbwebb.se/forum/posting.php?mode=reply&f=44&t=4552

On Cygwin doing backspace of an utf-8 character such as 'ö' will fail with
error message:

$ python3 test_input.py
-->
Traceback (most recent call last):
  File "p.py", line 8, in <module>
    a = input("-->")
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc3 in position 0:
unexpected end of data

"""

a = input("-->")

print(repr(a))
