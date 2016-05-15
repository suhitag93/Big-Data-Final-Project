#!/usr/bin/python

import sys
for line in sys.stdin:
    try:
        line = line.strip()
        if(len(line) != 0):
            inpline = line.split(',')
            snow = inpline[4]
            if (float(snow) != 0.0):
                print line
    except ValueError:
          continue