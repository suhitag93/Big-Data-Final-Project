#!/usr/bin/python

import sys
for line in sys.stdin:
    try:
        line = line.strip()
        if(len(line) != 0):
            inpline = line.split(',')
            temp = inpline[2]
            if (float(temp) != 'None'):
                print line
    except ValueError:
          continue