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


try:
    amount = float(stramount)
except ValueError:
    sys.exit("E: Couldn't parse amount: " + stramount)

c = sqlite3.connect(DB_FILE)
cur = c.cursor()

cur.execute("SELECT rowid, income FROM categories WHERE category LIKE ?", (category,))
try:
    (category_id, category_income) = cur.fetchone()
except TypeError:
    sys.exit("E: No such category")

if category_income == 0 or category_income == None:
    amount = -amount;

c.execute("INSERT INTO entries VALUES (?, NULL, ?, ?, ?, 0)",
                  (strdate, amount, description, category_id))

c.commit()
c.close()
