#!/usr/bin/python
import sys


        
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

#sys.stdin = open("data1.txt")

GC = []
GC.append(Point(float(27.772698),float(-82.682065)))
GC.append(Point(float(27.772641),float(-82.673911)))
GC.append(Point(float(27.768350),float(-82.674018)))
GC.append(Point(float(27.768350),float(-82.682108)))   
GCpoly = Polygon(GC)

RFC = []
RFC.append(Point(float(40.759720),float(-73.981730)))
RFC.append(Point(float(40.759996),float(-73.976215)))
RFC.append(Point(float(40.757379),float(-73.976451)))
RFC.append(Point(float(40.757331),float(-73.981129)))   
RFCpoly = Polygon(RFC)


PenSt = []
PenSt.append(Point(float(40.752958),float(-73.995312)))
PenSt.append(Point(float(40.753007),float(-73.989047)))
PenSt.append(Point(float(40.748829),float(-73.987910)))
PenSt.append(Point(float(40.748618),float(-73.992931)))   
PenStpoly = Polygon(PenSt)

PortAu = []
PortAu.append(Point(float(40.758728),float(-73.993896)))
PortAu.append(Point(float(40.759167),float(-73.988382)))
PortAu.append(Point(float(40.756046),float(-73.987545)))
PortAu.append(Point(float(40.755656),float(-73.993167)))   
PortAupoly = Polygon(PortAu)

TSQ = []
TSQ.append(Point(float(40.756372),float(-73.990334)))
TSQ.append(Point(float(40.756469),float(-73.986107)))
TSQ.append(Point(float(40.754031),float(-73.986064)))
TSQ.append(Point(float(40.754356),float(-73.990012)))   
TSQpoly = Polygon(TSQ)

        
for line in sys.stdin:
        line=line.strip()
        line=line.split(',')
        DateLocList=line[0].split('^')
        date = DateLocList[0]
        dLat = float(DateLocList[1])
        dLon = float(DateLocList[2])
        passCount = line[1]
        tripCount = line[2]
        #print date+","+dLat+","+dLon
        if GCpoly.contains(Point(dLat,dLon)):
                print  date+ ",GC\t" + passCount +","+ tripCount
        if RFCpoly.contains(Point(dLat,dLon)):
                print  date+ ",RFC\t" + passCount +","+ tripCount
        #        print str(dLat)+","+str(dLon)
        if PenStpoly.contains(Point(dLat,dLon)):
                print  date+ ",PEN\t" + passCount +","+ tripCount
        if PortAupoly.contains(Point(dLat,dLon)):
                print  date+ ",PORTAUTH\t" + passCount +","+ tripCount
        if TSQpoly.contains(Point(dLat,dLon)):
                print  date+ ",TSQ\t" + passCount +","+ tripCount
      
                




        


