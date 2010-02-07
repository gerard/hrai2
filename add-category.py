#!/usr/bin/env python

import sqlite3
import sys
import os


DB_PATH = os.getenv('HOME')
DB_FILE = DB_PATH + "/.hrai2.db"

try:
    cat_name = sys.argv[1]
except IndexError:
    sys.exit("Usage: " + sys.argv[0] + " date amount description")

c = sqlite3.connect(DB_FILE)

try:
    c.execute("INSERT INTO categories VALUES (?)", [(cat_name)])
except sqlite3.IntegrityError, detail:
    print "Integrity Error:", detail

c.commit()
c.close()
