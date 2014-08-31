#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Execute a .py-file that has the same filename as this file. 
A file hello.cgi will execute the file hello.py and wrap its
output with a HTTP header to be able to display the output as 
a webpage. 

"""


# To write pagecontent to sys.stdout as bytes instead of string
import sys
import codecs
import os


#Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()


# Send the HTTP header
print("Content-Type: text/plain;charset=utf-8")
#print("Content-Type: text/html;charset=utf-8")
print("")


# Here comes the content of the webpage 
# As a result from executin another python-script
filename = os.path.splitext(__file__)[0] + ".py"
fullpath = os.path.realpath(filename)

if os.path.isfile(fullpath) and os.access(fullpath, os.R_OK):
    
    # Write page content
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    
    exec(open(fullpath).read())

else:
    print("The file %s is not available, check if its there and set chmod to 644." % filename)
