#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check and verify locale settings to see if UTF-8 is output correctly.
"""

import sys
import locale
import os

print("Default encoding is (sys.getdefaultencoding()): ", sys.getdefaultencoding())
print("(sys.stdin.encoding):                           ", sys.stdin.encoding)
print("(sys.stdout.encoding):                          ", sys.stdout.encoding)
print("(sys.stderr.encoding):                          ", sys.stderr.encoding)

print("Default locale is (locale.getdefaultlocale()):  ", locale.getdefaultlocale())

print("Environment variable PYTHONIOENCODING: ", os.environ.get("PYTHONIOENCODING"))
print("Environment variable LANG:             ", os.environ.get("LANG")) 
print("Environment variable LC_CTYPE:         ", os.environ.get("LC_CTYPE"))

print("\u03b1\u03b2\u03b3")
print("░")

