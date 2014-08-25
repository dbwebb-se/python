#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Execute as cgi-skript and send a correct HTTP header.

"""



# Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()    



# Send the HTTP header for plain text or for html
print("Content-Type: text/plain;charset=utf-8")
#print("Content-Type: text/html;charset=utf-8")
print("")



# Here comes the content of the webpage 
print("Hello The World of Web")
