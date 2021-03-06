#!/usr/bin/env python

import sqlite3
import sys
import os
from datetime import datetime
from termcolor import colored
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-m", "--marked", action="store_true", dest="marked_flag",
                  default=False, help="Show only marked movements")
(options, args) = parser.parse_args()

DB_PATH = os.getenv('HOME')
DB_FILE = DB_PATH + "/.hrai2.db"

c = sqlite3.connect(DB_FILE)
cur = c.cursor()

query = """
SELECT e.rowid, e.amount, e.date, c.category, e.description, e.date_effective
FROM entries AS e, categories AS c
WHERE e.category = c.rowid
"""

# Marked list is sorted by the mark date and order of input
# Normal list is sorted by cost date and order of input
if options.marked_flag:
    query += " ORDER BY e.date_effective, marked"
else:
    query += " ORDER BY e.date, e.rowid"

cur.execute(query)
if cur.rowcount == 0:
    sys.exit(0)

total = 0

for line in cur.fetchall():
    id = line[0]
    amount = line[1]
    date = line[2]
    category = line[3]
    description = line[4]
    marked_date = line[5]

    if options.marked_flag and marked_date == None:
        continue

    if options.marked_flag:
        date = marked_date

    # If this fails it means db corruption!
    day = datetime.strptime(date, "%Y-%m-%d")
    if datetime.today() < day:
        date = colored(date, 'blue')
    else:
        wday = day.weekday()
        if wday == 5:
            date = colored(date, 'yellow')
        elif wday == 6:
            date = colored(date, 'red')
        else:
            date = colored(date, 'green')

    if marked_date == None:
        date = date + " "
    else:
        date = date + "*"

    if description == None:
        description = ""

    total += amount
    print '%06d'  % id, \
          '%9.2f' % total, ":", \
          '%9.2f' % amount, \
          date, \
          category.rjust(13) \
          , "=>", description

c.close()
