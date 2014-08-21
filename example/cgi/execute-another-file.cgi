#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Execute a .py-file that has the same filename as this file. 
A file hello.cgi will execute the file hello.py and wrap its
output with a HTTP header to be able to display the output as 
a webpage. 

"""

import os
import sys


#Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()    


# Send the HTTP header
print("Content-Type: text/plain;charset=utf-8")
#print("Content-Type: text/html;charset=utf-8")
print("")


# Here comes the content of the webpage 
# As a result from executin another python-script
#exec(open(os.path.dirname(os.path.realpath(__file__)) + "/mos-me.py").read())
#exec(open(os.path.splitext(__file__)[0] + ".py").read())
filename = os.path.splitext(__file__)[0] + ".py"
fullpath = os.path.realpath(filename)
exec(open(fullpath).read())
