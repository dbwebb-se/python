dict
==============================
Examples in Python 3


```python
"""
Creating a dictionary
"""
my_dict = {"apples": 3, "bananas": 5, "cherrys": 42}
print(my_dict)


"""
Accessing values in a dictionary
"""
print(my_dict["apples"])


"""
Changing valus
"""
my_dict["bananas"] += 1
my_dict["apples"] = 7
print(my_dict)


"""
Remove key
"""
del my_dict["cherrys"]
print(my_dict)


"""
Get iterable items for the dictionary
"""
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

# Iterate over key, value pairs
for key, value in my_dict.items():
    print("Key:", key, "; value:", value)


"""
Look for keys in dictionary
"""
print("apples" in my_dict)
print("lemons" in my_dict)




```


Reference and read more
------------------------------

[Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html?highlight=dict#mapping-types-dict)



Revision history
------------------------------

2014-07-21 (sylvanas) PA1 First try.
