#!/usr/bin/env python

import sys
import os

def run(bin):
    if os.path.exists(bin):
        cmd_line = bin
        for param in sys.argv[2:]:
            cmd_line += ' "' + param + '"'
        sys.exit(os.system(cmd_line))


try:
    cmd = sys.argv[1]
except IndexError:
    sys.exit("E: Usage: " + sys.argv[0] + " command [options]")

cmd_bin = [
    os.path.dirname(sys.argv[0]) + os.sep + cmd + ".py",
    os.path.dirname(sys.argv[0]) + os.sep + "../libexec" + os.sep + cmd + ".py"
]

for cmd_bin_try in cmd_bin:
    run(cmd_bin_try)

sys.exit("E: Couldn't find hrai2 installation")
