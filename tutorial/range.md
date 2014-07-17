range()
==============================
Examples in Python 3


```python
"""
Simple range of 10
"""
# Notice that it will not include 10, and starts at 0
print(range(10))
print("")


"""
Iterate over range
"""
for x in range(6):
	print(x, end=",")
print("\n")


"""
Change start for range
"""
for x in range(5,10):
	print(x, end=",")
print("\n")


"""
Add step to range
"""
# Only print even numbers
for x in range(0, 10, 2):
	print(x, end=",")
print("")


```


Reference and read more
------------------------------

[The range() Function](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)

[range()](https://docs.python.org/3/library/stdtypes.html#range)


Revision history
------------------------------

2014-07-17 (sylvanas) PA1 First try.
