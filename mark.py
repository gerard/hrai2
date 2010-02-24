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
    print "Usage: %s [-u] id [date]"
    sys.exit(1)

if options.unmark_flag:
    cur.execute("""
    UPDATE entries
    SET date_effective = NULL
    WHERE rowid = ? """, (id, ))
else:
    try:
        datetime.strptime(args[1], "%Y-%m-%d");
        mark_date = args[1]
    except:
        print "Usage: %s id date" % exec_name
        sys.exit(1)

    # Fetch the current maximum mark
    cur.execute("""
    SELECT MAX(marked)
    FROM entries
    WHERE date_effective = ?""", (mark_date,))

    max_mark = cur.fetchone()[0]
    if max_mark is None:
        next_mark = 0
    else:
        next_mark = max_mark + 1

    cur.execute("""
    UPDATE entries
    SET date_effective = ?, marked = ?
    WHERE rowid = ?""", (mark_date, next_mark, id))

c.commit();
c.close()
