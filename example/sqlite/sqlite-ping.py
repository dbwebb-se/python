#!/usr/bin/env python3
"""
Test example to take a ping and save it into an sqlite3 database
https://docs.python.org/3/library/sqlite3.html
"""
# pip install requests
import requests
import sqlite3
import time
import sys

# Get argument if there is one and use that as url
if len(sys.argv) == 2:
    url = sys.argv[1]
else:
    url = "http://dbwebb.se/"

# connect to the database and set a cursor
conn = sqlite3.connect("ping.sqlite3")
cur = conn.cursor()

# init database incase it's lost
cur.execute("""
CREATE TABLE IF NOT EXISTS Pings
(url TEXT, time TEXT PRIMARY KEY, repsonse INTEGER)""")

# get current time for logging
rTime = time.ctime(time.time())

try:
    # url must start with "http://" or the request fails
    r = requests.head(url)
    code = r.status_code
except requests.ConnectionError:
    code = 0

# create the values to be added as tuple
values = (url, rTime, code)
# insert values into database
cur.execute("""
INSERT INTO Pings (url, time, repsonse)
VALUES (?, ?, ?)
""", values)

print("Rows in db:")
# get all the rows in database
cur.execute("SELECT url, time, repsonse FROM Pings")
# loop through the result
for row in cur:
    print(row)

# commit the changes and close the connection
conn.commit()
conn.close()