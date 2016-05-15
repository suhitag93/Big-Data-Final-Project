#!/usr/bin/python

import sys

##sys.stdin=open("mapjoinout",'r')

prevKey=None
prevTag=None
List = []
for line in sys.stdin:
    #print line
    line = line.strip()
    key, value, tag  = line.split("\t")
    #print key,tag
    if (prevKey == key):
       if(prevTag == tag):
          List.append(value)
       elif(prevTag != tag):
          for i in List:
             if(tag == "W"):
                print key + '\t' + i + ',' + value
             else:
                print key + '\t' + value + ',' + i
    else:
        List = []
        List.append(value)
        prevKey = key
        prevTag = tag
