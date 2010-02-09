#!/usr/bin/env python

import sqlite3
import sys
import os


DB_PATH = os.getenv('HOME')
DB_FILE = DB_PATH + "/.hrai2.db"

c = sqlite3.connect(DB_FILE)
cur = c.cursor()

cur.execute("""
SELECT e.date, e.amount, c.category, e.description
FROM entries AS e, categories AS c
WHERE e.category = c.rowid
""")

total = 0
try:
    for line in cur.fetchall():
        total += line[1]
        print line[0], line[1], line[2], line[3], total
except TypeError:
    pass

c.close()
