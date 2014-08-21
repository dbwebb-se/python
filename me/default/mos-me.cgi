#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Execute a .py-file that has the same filename as this file. 
A file hello.cgi will execute the file hello.py and wrap its
output with a HTTP header to be able to display the output as 
a webpage. 

"""

import sys
import cgitb
import os

def enc_print(string='', encoding='utf8'):
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')

cgitb.enable()    


enc_print("Content-Type: text/plain")
enc_print("")
exec(open(os.path.dirname(os.path.realpath(__file__)) + "/mos-me.py").read())
