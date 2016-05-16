#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    key = line[0]
    value=line[1]
    for i in range(2,len(line)):
        value = value+","+line[i]
    print "%s\t%s" %(key,value)