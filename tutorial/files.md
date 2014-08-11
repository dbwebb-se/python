files
==============================
Examples in Python 3


```python
"""
Open file
"""
fhand = open("test.txt")
print(fhand)


"""
Read whole file
"""
print(fhand.read())


"""
Return to start of file
"""
fhand.seek(0)

"""
Read lines
"""
print(fhand.readline())
print(fhand.readline())


"""
Read all lines
"""
fhand.seek(0)
for line in fhand:
    print(line, end="")
print()

"""
Close file
"""
fhand.close()


"""
Write file
"""
# Open the file with appending mode
fhand = open("test.txt", "a")
inp = input("Enter what you want to add to the file: ")
fhand.write("\n" + inp)
fhand.close()

# Open the file for reading
fhand = open("test.txt")
print(fhand.read())
fhand.close()



```


Reference and read more
------------------------------

[Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)



Revision history
------------------------------

2014-07-21 (sylvanas) PA1 First try.
