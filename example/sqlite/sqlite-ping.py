#!/usr/bin/env python3
"""
Test example to take a ping and save it into an sqlite3 database
"""

import requests
import time
import sqlite3
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]
else:
    url = "http://dbwebb.se/"

conn = sqlite3.connect("ping.sqlite3")
cur = conn.cursor()

# init
# cur.execute("DROP TABLE IF EXISTS Pings")
# cur.execute("CREATE TABLE Pings (url TEXT, time TEXT PRIMARY KEY, repsonse INTEGER)")

rTime = time.ctime(time.time())

try:
    # url must start with "http://"
    r = requests.head(url)
    code = r.status_code
except requests.ConnectionError:
    code = 0

values = (url, rTime, code)
cur.execute("INSERT INTO Pings (url, time, repsonse) VALUES (?, ?, ?)", values)

print("Rows in db:")
cur.execute("SELECT url, time, repsonse FROM Pings")
for row in cur:
    print(row)


conn.commit()
conn.close()