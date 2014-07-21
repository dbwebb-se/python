String translation
==============================
Examples in Python 3



```python
# Need to import module to get access to string
import string

"""
Translate some characters into numbers
"""
# Create a variable string with all numbers 0-9
nrs = string.digits
# Create a string which containts characters for each number in order
# 		 0123456789
chars = "olzeasgtbp"

# Create a translation table, from and to as parameters
trans = str.maketrans(chars, nrs)

# Create a string to translate
my_str = "hello world"
# Use translate() and the table created to translate string
x = my_str.translate(trans)
print(x)



```


Reference and read more
------------------------------

[string — Common string operations](https://docs.python.org/3/library/string.html)


Revision history
------------------------------

2014-07-17 (sylvanas) PA1 First try.
