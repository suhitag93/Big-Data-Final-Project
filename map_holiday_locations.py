#!/usr/bin/python

import sys

holidaydates =["2015-01-01",
"2015-02-14",
"2015-07-04",
"2015-10-31",
"2015-11-26",
"2015-11-27",
"2015-12-24",
"2015-12-25",
"2015-12-31"]

class Point:
        def __init__(self,x,y):
                self.x = x
                self.y = y

class Polygon:
        def __init__(self,points):
                self.points = points
                self.nvert = len(points)

                minx = maxx = points[0].x
                miny = maxy = points[0].y
                for i in range(1,self.nvert):
                        minx = min(minx,points[i].x)
                        miny = min(miny,points[i].y)
                        maxx = max(maxx,points[i].x)
                        maxy = max(maxy,points[i].y)

                self.bound = (minx,miny,maxx,maxy)


        def contains(self,pt):
                firstX = self.points[0].x
                firstY = self.points[0].y
                testx = pt.x
                testy = pt.y
                c = False
                j = 0
                i = 1
                nvert = self.nvert
                while (i < nvert) :
                        vi = self.points[i]
                        vj = self.points[j]

                        if(((vi.y > testy) != (vj.y > testy)) and (testx < (vj.x - vi.x) * (testy - vi.y) / (vj.y - vi.y) + vi.x)):
                                c = not(c)

                        if(vi.x == firstX and vi.y == firstY):
                                i = i + 1
                                if (i < nvert):
                                        vi = self.points[i];
                                        firstX = vi.x;
                                        firstY = vi.y;
                        j = i
                        i = i + 1
                return c

        def bounds(self):
                return self.bound

polySTATENISLAND = Polygon([Point(40.640457, -74.124584),Point(40.636028, -74.157543),Point(40.635247, -74.193249),Point(40.596937, -74.199429),Point(40.557300, -74.215221),Point(40.507983, -74.255390),Point(40.494930, -74.237881),Point(40.546866, -74.112225),Point(40.599022, -74.052830),Point(40.646709, -74.075832),Point(40.640457, -74.124584)])
polyBROOKLYN = Polygon([Point(40.736165, -73.961077),Point(40.682648, -73.898678),Point(40.646709, -73.851643),Point(40.615182, -73.889751),Point(40.581033, -73.877735),Point(40.573731, -73.896961),Point(40.571124, -74.011631),Point(40.618310, -74.050083),Point(40.662337, -74.017124),Point(40.679263, -74.023647),Point(40.706596, -73.991718),Point(40.708157, -73.973179),Point(40.736165, -73.961077)])
polyQUEENS = Polygon([Point(40.736165, -73.961077),Point(40.682648, -73.898678),Point(40.646709, -73.851643),Point(40.593882, -73.824829),Point(40.554244, -73.947052),Point(40.537025, -73.942245),Point(40.537025, -73.942245),Point(40.622552, -73.765778),Point(40.656941, -73.720459),Point(40.750638, -73.703979),Point(40.801596, -73.822769),Point(40.776122, -73.935379),Point(40.736165, -73.961077)])
polyMANHATTAN = Polygon([Point(40.679263, -74.023647),Point(40.706596, -73.991718),Point(40.708157, -73.973179),Point(40.736165, -73.961077),Point(40.796398, -73.924393),Point(40.842126, -73.929886),Point(40.870690, -73.904480),Point(40.875363, -73.927826),Point(40.750118, -74.013657),Point(40.679263, -74.023647)])
polyBRONX = Polygon([Point(40.796398, -73.924393),Point(40.842126, -73.929886),Point(40.870690, -73.904480),Point(40.875363, -73.927826),Point(40.916291, -73.914413),Point(40.878088, -73.780472),Point(40.837840, -73.778412),Point(40.812380, -73.795921),Point(40.793669, -73.906471),Point(40.796398, -73.924393)])

#sys.stdin = open("droptest.txt","r")

for line in sys.stdin:
    try:
        #print line
        line = line.strip()
        key,passengers,count = line.split(",")
        #print key
        #print holidaydates
        date = str(key.split("^")[0])
        lat = float(key.split("^")[1])
        lon = float(key.split("^")[2])
        
        #print s1
        #print lat
        loc = Point(float(lat),float(lon))
        #print loc
        d_key = str(date)+"^"+str(lat)+"^"+str(lon)
        
        if polyMANHATTAN.contains(loc):
            if date in holidaydates: 
             print "%s^M\t%s" %(d_key,passengers)
        if polyBROOKLYN.contains(loc):
            if date in holidaydates:  
             print "%s^BK\t%s" %(d_key,passengers)
        if polyQUEENS.contains(loc):
            if date in holidaydates:  
             print "%s^Q\t%s" %(d_key,passengers)
        if polySTATENISLAND.contains(loc):
            if date in holidaydates:  
             print "%s^ST\t%s" %(d_key,passengers)
        if polyBRONX.contains(loc):
            if date in holidaydates:  
                print "%s^BX\t%s" %(d_key,passengers)

    except:
        pass
