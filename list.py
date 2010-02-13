#!/usr/bin/env python

import sqlite3
import sys
import os


DB_PATH = os.getenv('HOME')
DB_FILE = DB_PATH + "/.hrai2.db"

c = sqlite3.connect(DB_FILE)
cur = c.cursor()

cur.execute("""
SELECT e.amount, e.date, c.category, e.description
FROM entries AS e, categories AS c
WHERE e.category = c.rowid
ORDER BY e.date_effective
""")

total = 0
try:
    for line in cur.fetchall():
        total += line[0]
        print '%9.2f' % total, ":", '%9.2f' % line[0], line[1], line[2].rjust(12), "=>", line[3]
except TypeError:
    pass

c.close()
