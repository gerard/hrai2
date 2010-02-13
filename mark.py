#!/usr/bin/env python

import sqlite3
import sys
import os
from datetime import datetime
from termcolor import colored
from optparse import OptionParser

exec_name = sys.argv[0]
parser = OptionParser()
parser.add_option("-u", "--unmark", action="store_true", dest="unmark_flag",
                  default=False, help="Unmark instead of marking")
(options, args) = parser.parse_args()

DB_PATH = os.getenv('HOME')
DB_FILE = DB_PATH + "/.hrai2.db"

c = sqlite3.connect(DB_FILE)
cur = c.cursor()

try:
    id = int(args[0])
except:
    print "Usage: %s id" % exec_name
    sys.exit(1)

if options.unmark_flag:
    mark = 0
else:
    mark = 1

cur.execute("""
UPDATE entries
SET marked = ?
WHERE rowid = ? """, (mark, id))

c.commit();
c.close()
