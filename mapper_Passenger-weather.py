#!/usr/bin/python

import sys
#sys.stdin = open("mapjoinout.txt")
for line in sys.stdin:
    try:
        line = line.strip()
        if(len(line) != 0):
            key,valueLine = line.split('\t')
            valueLine = valueLine.split(",")
            #print valueLine
            temp = valueLine[24]
            #print temp
            pcp = valueLine[28]
            snow = valueLine[29]

            if(temp == "None"):
                temp = valueLine[30]

            if(pcp == "None"):
                pcp = valueLine[32]

            if(snow == "None"):
                snow = 0.0

            passengers = int(valueLine[3])
            weatherMetrics = temp+','+ pcp +','+ str(snow)
            value= str(passengers) +','+weatherMetrics
            print key + '\t' + value

    except ValueError:
          continue
