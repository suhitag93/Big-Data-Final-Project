#!/usr/bin/python

import sys

try:
    for line in  sys.stdin:
        line = line.strip()
        key,value = line.split("\t")
        date = key.split("^")[0]
        value = value.split(",")
        #plat = (value[6])
        #plon = (value[5])
        dlat = (value[10])
        dlon = (value[9])
        psgr = int(value[3])
        dist = float(value[4])
        #pickup = "("+str(plat)+":"+plon+")"
        drop = date+"^"+str(dlat)+"^"+str(dlon)

        print "%s\t%s"%(drop,psgr)

except:
    pass

