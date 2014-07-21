String methods
==============================
Examples in Python 3


```python
"""
Transforming case
"""

# Capitalize
x = "hello"
y = x.capitalize()
print(y)

# Uppercase
y = x.upper()
print(y)

# Lowercase
x = "HeLLo"
y = x.lower()
print(y)


"""
Transforming encoding
"""
# Encode to unicode
x = "me@mail.com // 30€"
y = x.encode()
print(y)


"""
Replacing, splitting and joining
"""

# Replace parts
x = "Hello"
y = x.replace("l", "y")
print(y)

# Split
x = "I like trains"
y = x.split()
print(y)		# Iterable list retured from split

# Join
x = ["So", "long", "and", "thanks", "for", "all", "the", "fish"]
separator = " "
y = separator.join(x)
print(y)


"""
Searching a string
"""
x = "Applepie"
y = x.index("pie")
print(y)
print(x[y:])

y = x.find("pine")
print(y)		# Not found




```


Reference and read more
------------------------------

[String Methods](https://docs.python.org/3/library/stdtypes.html?highlight=string#text-sequence-type-str)



Revision history
------------------------------

2014-07-17 (sylvanas) PA1 First try.
