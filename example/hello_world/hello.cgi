#!/usr/bin/env python3

import sys
import cgitb
import os

def enc_print(string='', encoding='utf8'):
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')

cgitb.enable()    


enc_print("Content-Type: text/plain")
enc_print("")
exec(open(os.path.dirname(os.path.realpath(__file__)) + "/hello.py").read())
