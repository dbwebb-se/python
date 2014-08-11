while
==============================
Examples in Python 3


```python
"""
Loop until x is certain value
"""
x = 0
while x < 10:
	x += 3
	print(x)


"""
Loop until x is certain value with while True and break
"""
x = 0
while True:
	x += 3
	print(x)
	if x > 10:
		break


"""
More useful while with break (nothing to iterate over) - take input until input is "done"
"""
my_str = ""
while True:
	inp = input("> ")
	if inp == "done":
		break
	my_str += inp
print(my_str)



```


Reference and read more
------------------------------

[The while statement](https://docs.python.org/3/reference/compound_stmts.html?highlight=while#while)

[While loops](https://wiki.python.org/moin/WhileLoop)



Revision history
------------------------------

2014-07-17 (sylvanas) PA1 First try.
