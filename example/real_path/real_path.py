#!/usr/bin/env python3
"""
How to get absolute path for current directory
"""
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
