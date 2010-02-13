#!/usr/bin/env python

import sqlite3
from datetime import datetime
import sys
import os
from optparse import OptionParser


DB_PATH = os.getenv('HOME')
DB_FILE = DB_PATH + "/.hrai2.db"
exec_name = sys.argv[0]

parser = OptionParser()
parser.add_option("-e", "--effective-date", dest="effective_date",
                  default=None, help="Set effective date")
(options, args) = parser.parse_args()


def parse_date_with_exc(strdate):
    try:
        return datetime.strptime(strdate, "%Y-%m-%d")
    except:
        sys.exit("E: Couldn't parse date: " + strdate)

try:
    strdate = args[0]
    stramount = args[1]
    category = args[2]
except IndexError:
    sys.exit("E: Usage: " + exec_name + " date amount category description")

try:
    description = args[3]
except:
    description = None

parse_date_with_exc(strdate)

if options.effective_date:
    effective = options.effective_date
    parse_date_with_exc(effective);
else:
    effective = strdate

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

c.execute("INSERT INTO entries VALUES (?, ?, ?, ?, ?)",
                  (strdate, effective, amount, description, category_id))

c.commit()
c.close()
