#!/usr/bin/env python

import sys
import os

try:
    cmd = sys.argv[1]
except IndexError:
    sys.exit("E: Usage: " + sys.argv[0] + " command [options]")

cmd_bin = os.path.dirname(sys.argv[0]) + os.sep + cmd + ".py"
if os.path.exists(cmd_bin):
    os.system(cmd_bin + " " + ' '.join(sys.argv[2:]))
    sys.exit(0)

cmd_bin = os.path.dirname(sys.argv[0]) + os.sep + "../libexec" \
                                       + os.sep + cmd + ".py"
if os.path.exists(cmd_bin):
    os.system(cmd_bin + " " + ' '.join(sys.argv[2:]))
    sys.exit(0)

sys.exit("E: Couldn't find hrai2 installation")
