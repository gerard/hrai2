#!/usr/bin/env python

import sqlite3
import sys
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--force", action="store_true", dest="force_flag",
                  default=False, help="Overwrite existing DB")
(options, args) = parser.parse_args()


DB_PATH = os.getenv('HOME')
DB_FILE = DB_PATH + "/.hrai2.db"

if os.path.exists(DB_FILE) and options.force_flag == False:
    sys.exit("E: DB File exists. Use --force to override")

os.unlink(DB_FILE)
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()

c.execute("""
CREATE TABLE entries (
    date TEXT,
    date_effective TEXT,
    amount INTEGER,
    description TEXT,
    category INTEGER,
    marked INTEGER
)
""")

c.execute("""
CREATE TABLE categories (
    category TEXT UNIQUE,
    income INTEGER
)
""")

conn.commit()
c.close()
