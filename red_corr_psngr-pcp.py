#!/usr/bin/python
import sys
import math

psngrList = []
pcpList = []
count=0
sumPsngr=0
sumPcp=0.0
#sys.stdin = open("newForCorrelation.txt",'r')

def pearsonCoefficient(x, y, avgX, avgY):
    xDif2 = 0.0
    yDif2 = 0.0
    difPrd = 0.0
    for i in range(len(x)):
        xDif = x[i] - avgX
        yDif = y[i] - avgY
        difPrd+= xDif*yDif
        xDif2+= xDif*xDif
        yDif2+= yDif*yDif
    return difPrd / math.sqrt(xDif2 * yDif2)

for line in sys.stdin:
    line=line.strip()

    value= line.split(',')

    sumPsngr = sumPsngr + float(value[1])
    sumPcp = sumPcp + float(value[3])
    count+=1
    psngrList.append(float(value[1]))
    pcpList.append(float(value[3]))

averagePsngr = float(sumPsngr/count)
averagePcp = float(sumPcp/count)

print "Pearson's Coefficient: "
print "Passengers v/s Precipitation:"
print pearsonCoefficient(psngrList,pcpList,averagePsngr,averagePcp)