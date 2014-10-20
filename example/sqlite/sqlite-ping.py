#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Is the website alive? This could be tested at a regular interval by retrieving 
a url and checking its status. These tests can be stored in a database which makes
it easy to accumulate statistics and to query for various patterns.

Manual:
  https://docs.python.org/3/library/sqlite3.html

The database is named "ping.db" and is stored in the current directory.

If you have the command "sqlite3" installed you could use that to connect to the 
database and inspect it.

$ sqlite3 ping.db 

"""

import requests
import sqlite3
import time
import sys



def isSQLite3(filename):
    """
    Check if a file is a SQLite3 database.
    http://stackoverflow.com/questions/12932607/how-to-check-with-python-and-sqlite3-if-one-sqlite-database-file-exists
    """
    from os.path import isfile, getsize

    if not isfile(filename):
        return False
    if getsize(filename) < 100: # SQLite database file header is 100 bytes
        return False
    else:
        fd = open(filename, 'rb')
        Header = fd.read(100)
        fd.close()

        if Header[0:16] == b'SQLite format 3\000':
            return True
        else:
            return False


#
# Get argument if there is one and use that as url
#
if len(sys.argv) == 2:
    url = sys.argv[1]
else:
    sys.stderr.write("Add the url (for example http://bth.se) to check as a command line argument.\n")
    sys.stderr.write("{command} http://bth.se.\n\n".format(command=sys.argv[0]))
    sys.exit(1)



print(__doc__)
input("Press enter to continue.")



#
# Connect to the database and set a cursor
#
dbFile = "ping.db"

db = sqlite3.connect(dbFile)
dbc = db.cursor()


#
# Init a new database if needed
#
dbc.execute("CREATE TABLE IF NOT EXISTS Pings (url TEXT, time TEXT, response INTEGER)")


#
# Check if the database is valid
#
if not isSQLite3(dbFile):
    sys.stderr.write("The file '{}' is not a valid SQLite database.\n".format(dbFile))
    sys.exit(1)



#
# get current time for logging
#
rTime = time.ctime(time.time())

try:
    # url must start with "http://" or the request fails
    print("Connecting to: {}".format(url))
    r = requests.head(url, timeout=5)
    code = r.status_code

except requests.ConnectionError:
    code = 0



#
# insert values into database
#
print("Storing log entry in database")
aTuple = (url, rTime, code)
dbc.execute("INSERT INTO Pings (url, time, response) VALUES (?, ?, ?)", aTuple)

print("Retrieving all rows in database:")
dbc.execute("SELECT url, time, response FROM Pings")

# Loop through a resultset from a SELECT query
for row in dbc:
    print(row)



#
# Commit the changes and close the connection
#
db.commit()
db.close()
