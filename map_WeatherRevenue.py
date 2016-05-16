#!/usr/bin/python

import sys
#sys.stdin = open("mapjoinout.txt")
for line in sys.stdin:
    try:
        line = line.strip()
        if(len(line) != 0):
            line = line.split('\t')
            key = line[0].split('^')[0]
            valueLine = line[1].split(',')
            temp = valueLine[24]
            pcp = valueLine[28]
            snow = valueLine[29]

            if(temp == "None"):
                temp = valueLine[30]

            if(pcp == "None"):
                pcp = valueLine[32]

            if(snow == "None"):
                snow = 0.0

            totRev = float(valueLine[12])+float(valueLine[15])+float(valueLine[17])
            weatherMetrics = temp+','+ pcp +','+ str(snow)
            value= str(totRev) +','+weatherMetrics;
            print key + '\t' + value

    except ValueError:
          continue
