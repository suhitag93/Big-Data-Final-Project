#!/usr/bin/python
import sys
import math

psngrList = []
tempList = []
count=0
sumPsngr=0
sumTemp=0.0

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
    sumTemp = sumTemp + float(value[2])
    count+=1
    psngrList.append(float(value[1]))
    tempList.append(float(value[2]))

averagePsngr = sumPsngr/count
averageTemp = sumTemp/count

print "Pearson's Coefficient: "
print "Passengers v/s Temperature:"
print pearsonCoefficient(psngrList,tempList,averagePsngr,averageTemp)