#!/usr/bin/python
import sys

for line in sys.stdin:
    line =line.strip()
    key,value =line.split("\t")
    print "%s\t%s" %(key,value)
