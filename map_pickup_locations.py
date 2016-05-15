#!/usr/bin/python

import sys
#sys.stdin = open("mapjoinout.txt")

for line in  sys.stdin:
    try:
        line = line.strip()
        key,value = line.split("\t")
        date = key.split("^")[0]
        value = value.split(",")

        plat = (value[6])
        plon = (value[5])

        psgr = int(value[3])
        dist = float(value[4])

        pickup = date +"^" +str(plat)+"^"+str(plon)
        #drop = "("+str(plat)+":"+plon+")"

        print "%s\t%s"%(pickup,psgr)

    except:
        pass

