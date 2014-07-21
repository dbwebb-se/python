list - basics
==============================
Examples in Python 3


```python
"""
Simple list of integers
"""
my_list = [1,2,3,4,5]
print(my_list)


"""
Indexing
"""
print(my_list[0])
print(my_list[4])
print(my_list[-1])


"""
Slicing
"""
print(my_list[:2])
print(my_list[3:5])
print(my_list[2:])


"""
Copying lists
"""
# What happenes if we just copy the variable?
my_list = [1,2,3,4,5]
copy = my_list
copy[0] = 42
print("Copy:", copy)     
print("My list:", my_list)  # Both are the same even though we only changed one!

# Check the reference of copy and my_list
print("Copy has the same reference as my_list:", copy is my_list)


# Copy list my using slice
my_list = [1,2,3,4,5]
copy = my_list[:]
copy[0] = "42"
print("Copy:", copy)
print("My list:", my_list)  # Now only copy was changed, the reference was no longer the same

# Check that the reference to copy and my_list are NOT the same
print("Copy has the same reference as my_list:", copy is my_list)


"""
Merge lists
"""
x = [1,2,3]
y = ["apple", "banana"]
x += y
print(x)



"""
Replace and remove
"""
# Replace and add more
x = ["apple", "banana", "cherry", "date"]
x[2:4] = ["blueberry", "blackcurrant", "cocunut", "cranberry", "cantaloupe"]
print(x)

# Remove
x[3:5] = []
print(x)



```


Reference and read more
------------------------------

[Tutorial - Lists](https://docs.python.org/3/tutorial/introduction.html#lists)



Revision history
------------------------------

2014-07-21 (sylvanas) PA1 First try.
