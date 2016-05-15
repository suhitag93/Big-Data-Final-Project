#!/usr/bin/python

import sys
#sys.stdin = open("newForCorrelation.txt")
for line in sys.stdin:
    try:
        line = line.strip()
        if(len(line) != 0):
            inpline = line.split(',')
            pcp = inpline[3]
            if (float(pcp) > 0.00):
                print line
    except ValueError:
          continue
