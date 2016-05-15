#!/usr/bin/python

import sys
import math

revList = []
tempList = []
count=0
sumRev=0.0
sumTemp=0.0
#sys.stdin = open("newForCorrelation.txt",'r')

def pearsonCoefficient(rev, pcp, avgX, avgY):
    xDif2 = 0.0
    yDif2 = 0.0
    difPrd = 0.0
    for i in range(len(rev)):
        xDif = rev[i] - avgX
        yDif = pcp[i] - avgY
        difPrd+= xDif*yDif
        xDif2+= xDif*xDif
        yDif2+= yDif*yDif
    return difPrd / math.sqrt(xDif2 * yDif2)

for line in sys.stdin:
    line=line.strip()
    #line=line.split('\t')
    valueL= line.split(',')

    sumRev = sumRev + float(valueL[1])
    sumTemp = sumTemp + float(valueL[2])
    count+=1
    revList.append(float(valueL[1]))
    tempList.append(float(valueL[2]))


averageRev= sumRev/count
averageTemp= sumTemp/count


print pearsonCoefficient(revList,tempList,averageRev,averageTemp)
