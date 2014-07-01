#!/usr/bin/env python3

import sys
import cgitb

def enc_print(string='', encoding='utf8'):
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')

cgitb.enable()    


enc_print("Content-Type: text/html")
enc_print("""
<!doctype html>
<meta charset="utf-8">
<title>Min me-sida</title>
<h1>Min Me-sida</h1>
<p>Hej, jag heter Mikael Roos och är lärare på denna kursen.</p>
""")
