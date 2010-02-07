#!/usr/bin/env python

import sqlite3
from datetime import datetime
import sys
import os


DB_PATH = os.getenv('HOME')
DB_FILE = DB_PATH + "/.hrai2.db"

try:
    strdate = sys.argv[1]
    stramount = sys.argv[2]
    category = sys.argv[3]
    description = sys.argv[4]
except IndexError:
    sys.exit("E: Usage: " + sys.argv[0] + " date amount category description")

try:
    datetime.strptime(strdate, "%Y-%m-%d")
except ValueError:
    sys.exit("E: Couldn't parse date: " + strdate)

try:
    amount = float(stramount)
except ValueError:
    sys.exit("E: Couldn't parse amount: " + stramount)

c = sqlite3.connect(DB_FILE)
cur = c.cursor()

cur.execute("SELECT rowid FROM categories WHERE category LIKE ?", (category,))
try:
    category_id = cur.fetchone()[0]
except TypeError:
    sys.exit("E: No such category")

c.execute("INSERT INTO entries VALUES (?, ?, ?, ?)", 
                                      (strdate, amount, description, category_id))

c.commit()
c.close()
