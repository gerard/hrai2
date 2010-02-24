#!/usr/bin/env python

from datetime import datetime
import gzip
import sys
import os


DB_PATH = os.getenv('HOME')
DB_FILE = DB_PATH + os.sep + ".hrai2.db"

today = datetime.today()
datestamp = str(today.year) + '%02d' % today.month + '%02d' % today.day
DB_BACKUP = DB_FILE + ".backup" + os.sep + "hrai2.db." + datestamp + ".gz"

f_in = open(DB_FILE, 'rb')
f_out = gzip.open(DB_BACKUP, 'wb')
f_out.writelines(f_in)

f_out.close()
f_in.close()

sys.exit(0)
