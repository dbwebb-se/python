#!/usr/bin/env python3
"""
Example of how to read the content of a file into a list
"""

# the name of the file
filename = "items.txt"

# with - as for reading a file automatically closes it after reading is done
with open(filename) as filehandle:
    line = filehandle.readline()
# print the line read from the file
print(line)


# split the line into a list on the comma ","
items_as_list = line.split(",")
# print what the list looks like
print(items_as_list)


# add item to the list
items_as_list.append("cup")
# print what the list looks like after change
print(items_as_list)


# join the list into a string with a comma ","" between every item
list_as_str = ",".join(items_as_list)
# show what the string looks like after join
print(list_as_str)


# write the line to the file
with open(filename, "w") as filehandle:
    filehandle.write(list_as_str)
