FAQ - Differences between Python 2 and 3
==============================


```python
"""
Print
"""
# Python 2
print "Hello world!"

print "text", ; print "print more text on the same line"

# Python 3
print("Hello world!")

print("some text,", end="") 
print(" print more text on the same line")


"""
Input
"""
# Python 2
inp = raw_input("Enter your input: ")

# Python 3
inp = input("Enter your input: ")


"""
Division
"""
# Python 2
x = 5 / 4
print x		# prints 1, an integer

# Python 3
x = 5 / 4
print(x)	# prints 1.25, a float

x = 5 // 4
print(x)	# prints 1, an integer


"""
Type
"""
# Python 2
x = 42
type(x)		# prints <type 'int'>

# Python 3
x = 42
type(x)		# prints <class 'int'>


"""
Range
"""
# Python 2
for x in xrange(10):	# xrange() is faster than range()
	print x,

# Python 3
for x in range(10):		# xrange() no longer exists
	print(x, end=" ")


"""

"""
# Python 2

# Python 3


```



Reference and read more
------------------------------

[What’s New In Python 3.0](https://docs.python.org/3/whatsnew/3.0.html)



Revision history
------------------------------

2014-07-15 (sylvanas) PA1 First try.

