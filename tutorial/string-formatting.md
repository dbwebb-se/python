Formatting strings and output
==============================
str.format() in Python 3

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
f-string formatting in Python 3
```python
""" 
Python 3.6 added support for new kind of formatting. 
"""
# The syntax is similar to the one you used with str.format() but less verbose and also faster.
name = "John"
f"Hello, {name}"

# F-strings are evaluated at runtime, you can put any and all valid Python expressions in them.
f"1 + 1 = {1+1}"

# You could also call functions 
def to_lowercase(string):
    return string.lower()

f"My name is {to_lowercase("John")} at lower-case"

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
