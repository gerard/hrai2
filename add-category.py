#!/usr/bin/env python

import sqlite3
import sys
import os
from optparse import OptionParser

exec_name = sys.argv[0]
parser = OptionParser()
parser.add_option("-i", "--income", action="store_true", dest="income_flag",
                  default=False, help="Category defaults to income")
(options, args) = parser.parse_args()


DB_PATH = os.getenv('HOME')
DB_FILE = DB_PATH + "/.hrai2.db"

try:
    cat_name = args[0]
except IndexError:
    sys.exit("Usage: " + exec_name + " category")

if options.income_flag:
    cat_income = 1
else:
    cat_income = 0

c = sqlite3.connect(DB_FILE)

try:
    c.execute("INSERT INTO categories VALUES (?, ?)", (cat_name, cat_income))
except sqlite3.IntegrityError, detail:
    print "Integrity Error:", detail

c.commit()
c.close()
