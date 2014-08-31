#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Me-page redovisning, texts from each course moment.
As cgi.

"""


# To write pagecontent to sys.stdout as bytes instead of string
import sys
import codecs


#Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()    


# Send the HTTP header
print("Content-Type: text/plain;charset=utf-8")
#print("Content-Type: text/html;charset=utf-8")
print("")


# Here comes the content of the webpage 
content = """
Min Redovisnings-sida
==============================================================================


Kmom01:
------------------------------------------------------------------------------

Här skriver du redovisningstext för kursmoment 01.


Kmom02:
------------------------------------------------------------------------------

Här skriver du redovisningstext för kursmoment 02.

Osv.


"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content)
