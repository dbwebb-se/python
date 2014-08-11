If, elif, else
==============================
Examples in Python 3


```python
"""
Do something if a variable has a certain value.
"""
val = True

if val:
	print("YES")

# Above is the same as this
if val == True:
	print("YES")


"""
Add an else statement.
"""
if val:
	print("YES")
else:
	print("NO")


"""
Use many if-tests.
"""
if val == True:
	print("TRUE")
elif val == False:
	print("FALSE")
elif val == None:
	print("NONE")
else:
	print("NO")


```



Reference and read more
------------------------------

[if Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)



Revision history
------------------------------

2014.07-15 (sylvanas) PA2 Second try, now with Python syntax.

2014-06-02 (mos) PA1 First try.

