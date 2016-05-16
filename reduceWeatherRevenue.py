#!/usr/bin/python
import sys
#import math
flag="-1"
prevKey="0"
rev=0
temp=0
pcp=0
snow=0
currKey="0"
count =0
snowList = []
#sys.stdin = open("new2.txt",'r')
for line in sys.stdin:
    try:
       line=line.strip()
       line=line.split('\t')
       valueLine= line[1].split(',')
       currKey=line[0]
       if(flag== "-1"):
          prevKey=line[0]
          rev=float(valueLine[0])
          temp=float(valueLine[1])
          pcp=float(valueLine[2])
          snow=float(valueLine[3])
          snowList.append(snow)
          count+=1
          flag="1"
          continue
       if(prevKey==currKey):
          rev=float(rev)+ float(valueLine[0])
          temp=float(temp)+ float(valueLine[1])
          pcp=float(pcp)+ float(valueLine[2])
          snow=float(valueLine[3])
          snowList.append(snow)
          count+=1
          #snow=float(snow)+ float(line[3])
       else:
          maxSnow= max(snowList)
          temp = temp/count
          pcp = pcp/count
          print "%s,%.2f,%.2f,%.2f,%.2f" %(prevKey,rev,temp,pcp,maxSnow)
          snowList = []
          prevKey=currKey
          count=0
          rev=float(valueLine[0])
          temp=float(valueLine[1])
          pcp=float(valueLine[2])
          snow=float(valueLine[3])
          count+=1
          snowList.append(snow)
    except ValueError:
          continue
maxSnow= max(snowList)
temp = temp/count
pcp = pcp/count
print "%s,%.2f,%.2f,%.2f,%.2f" %(prevKey,rev,temp,pcp,maxSnow)
