#!/usr/bin/python
import sys
#import math
flag="-1"
prevKey="0"
passC=0
tripC=0
currKey=""
tag=""
#sys.stdin = open("data2.txt",'r')
for line in sys.stdin:
    try:
       line=line.strip()
       line=line.split('\t')
       valueLine= line[1].split(',')
       currKey=line[0]
       if(flag== "-1"):
          prevKey=line[0]
          passC=int(valueLine[0])
          tripC=int(valueLine[1])
          flag="1"
          continue
       if(prevKey==currKey):
          passC=int(passC)+ int(valueLine[0])
          tripC=int(tripC)+ int(valueLine[1])
       else:
          print "%s,%d,%d" %(prevKey,passC,tripC)
          prevKey=currKey
          passC=int(valueLine[0])
          tripC=int(valueLine[1])
    except ValueError:
          continue
print "%s,%d,%d" %(prevKey,passC,tripC)
