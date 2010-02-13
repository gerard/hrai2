#!/usr/bin/env python

import sqlite3
import sys
import os
from datetime import datetime
from termcolor import colored


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

if cur.rowcount == 0:
    sys.exit(0)

total = 0

for line in cur.fetchall():
    amount = line[0]
    date = line[1]
    category = line[2]
    description = line[3]

    # If this fails it means db corruption!
    wday = datetime.strptime(date, "%Y-%m-%d").weekday()

    if wday == 5:
        date = colored(date, 'yellow')
    elif wday == 6:
        date = colored(date, 'red')
    else:
        date = colored(date, 'green')

    total += amount
    print '%9.2f' % total, ":", \
          '%9.2f' % amount, \
          date, \
          category.rjust(12) \
          , "=>", description

c.close()
