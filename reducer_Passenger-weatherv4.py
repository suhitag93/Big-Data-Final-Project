#!/usr/bin/python

import sys
import os
flag=False
prevKey="0"
psngr=0
temp=0
pcp=0
max_snow=0
prevKey=None
count =0

#sys.stdin = open('map_pw','r')

for line in sys.stdin:
    try:
       line=line.strip()
       line=line.split('\t')
       valueLine= line[1].split(',')
       currKey=line[0]

       if(flag== False):
          prevKey=currKey        #initialize prevKey with first key to enter reduce task
          psngr=int(valueLine[0])
          temp=float(valueLine[1])
          pcp=float(valueLine[2])
          max_snow=float(valueLine[3])
          snow = max_snow
          count+=1
          flag=True
          continue         #skip the rest of the loop

       if(prevKey == currKey):
          psngr=int(psngr)+ int(valueLine[0])
          temp=float(temp)+ float(valueLine[1])
          pcp=float(pcp)+ float(valueLine[2])
          snow = float(valueLine[3])
          if max_snow <snow:
              max_snow = snow
          count+=1
       else:
          temp = temp/count
          pcp = pcp/count
          print "%s,%.2f,%.2f,%.2f,%.2f" %(prevKey,psngr,temp,pcp,max_snow)

          prevKey=currKey
          count=0
          count+=1
          psngr=int(valueLine[0])
          temp=float(valueLine[1])
          pcp=float(valueLine[2])
          max_snow = float(valueLine[3])
    except ValueError:
          continue
temp = temp/count
pcp = pcp/count
print "%s,%s,%.2f,%.2f,%.2f" %(prevKey,psngr,temp,pcp,max_snow)
