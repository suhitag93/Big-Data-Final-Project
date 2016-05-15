#!/usr/bin/python

import sys
#sys.stdin = open("newForCorrelation.txt")
for line in sys.stdin:
    try:
        line = line.strip()
        if(len(line) != 0):
            inpline = line.split(',')
            temp = inpline[2]
            if (float(temp) > 0.00):
                print line
    except ValueError:
          continue
