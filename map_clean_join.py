#!/usr/bin/python
import sys
import math

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

#create NYC polygon
NYCpoly = Polygon ([Point(40.873233, -73.966983), Point(40.788547, -73.780216),
                    Point(40.541669, -73.912738), Point(40.683449, -74.260868), Point(40.873233,-73.966983)])

for line in sys.stdin:

    try:
        flag = True
        line = line.strip()
        key,values = line.split("\t")
        valueList = values.split(",")
        #print valueList
        time = valueList[0]
        distance = float(valueList[4])
        passengers = float(valueList[3])
        plat = float(valueList[6])
        plon = float(valueList[5])
        pickup =Point(plat,plon)
        dlat = float(valueList[10])
        dlon = float(valueList[9])
        drop = Point(dlat,dlon)
        #print flag
        if NYCpoly.contains(pickup) and NYCpoly.contains(drop):
            print "%s\t%s" %(key,values)

    except:
        pass