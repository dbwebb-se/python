#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example code for modules v2.
"""

import sandwich as s

ingredients = ["ost", "bacon", "sallad", "majonnäs"]
ingredients_string = s.create_sandwich_string(ingredients, "En BLT innehåller")
print(ingredients_string)
