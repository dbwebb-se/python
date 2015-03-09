Formatting strings and output
==============================
Examples in Python 3


```python
"""
Format strings for fancier output
"""
# Add variable values to a string
x = "{0} ants are more than {1} elephants".format("Five", 4)
print(x)

x = "Five"
y = 4
print("{0} ants are more than {1} elephants".format(x, y))

# With named parameters
print("My name is {name} and I am {age} years old.".format(age=18, name="Mumintrollet"))

# Add thousands separator
print("{:,}".format(1000000))

# Fixed floating point
print("{:.2f}".format(1.2345))

print("{:.3f}".format(42))

# Fixed character width
print("{0:10}{1:10}".format("Hello", "World"))


```



Reference and read more
------------------------------

[String Formatting](https://docs.python.org/3/library/string.html#string-formatting)

[Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings)

[str.format()](https://docs.python.org/3/library/stdtypes.html#str.format)

[Fancier Output Formatting](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting)


Revision history
------------------------------

2014-07-16 (sylvanas) PA1 First try.
