#!/usr/bin/python

import sys
#sys.stdin = open("newForCorrelation.txt")
for line in sys.stdin:
    try:
        line = line.strip()
        if(len(line) != 0):
            inpline = line.split(',')
            snow = inpline[4]
            if (float(snow) > 0.00):
                print line
    except ValueError:
          continue
