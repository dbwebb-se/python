try-except
==============================
Examples in Python 3


```python
"""
Try-except example with string to integer conversion
"""
# The string is numeric - int() will succeed
x = "42"
print(x, "is of type", type(x))

try:
	x = int(x)
	print(x, "is of type", type(x))
except:
	print("Could not convert", x, "to integer")

print(x, "is the answer to everything\n")


# The string is not numeric - int() will fail and throw an exception
x = "fortytwo"
print(x, "is of type", type(x))

try:
	x = int(x)
	print(x, "is of type", type(x))
except:
	print("Could not convert", x, "to integer")

print(x, "is the answer to everything")
	


```


Reference and read more
------------------------------

[Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)

[The try statement](https://docs.python.org/3/reference/compound_stmts.html#try)


Revision history
------------------------------

2014-07-17 (sylvanas) PA1 First try.
