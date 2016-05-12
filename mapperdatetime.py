#!/usr/bin/python

import sys

#from shapely.geometry import Point, Polygon

#sys.stdin = open("yellow_tripdata_2015-01.csv")
#sys.stdin = open("map_out")

#mapreduce_map_input_file = os.environ.get("mapreduce_map_input_file")

#create NYC polygon:
#NYC = Polygon(((40.873233, -73.966983), (40.788547, -73.780216), (40.541669, -73.912738), (40.683449, -74.260868),
 #         (40.873233, -73.966983)))

for line in sys.stdin:         #for line in open(mapreduce_map_input_file):

    line = line.strip()
    line = line.split(',')
    #print len(line)
    #print line[0].isdigit()
    if ((line[0].isdigit()) and len(line)==19):       #trip data
        date,time = line[1].split()
        hr = time.split(":")[0]
        #key created of date-hour from trip start:
        date_hr = date+"^"+hr
        value = time
        #pickup lat, long
        #pick_up = Point(float(line[6]),float(line[5]))
        #drop off lat, long
        #drop_off = Point(float(line[10]),float(line[9]))
        #if NYC.contains(pick_up) or NYC.contains(drop_off):
         #   in_nyc = True
        for i in range(0,len(line)):
             if(i!=1):
                value = value+","+str(line[i])
        print "%s\t%s\tT" %(date_hr,value)
    elif (len(line)==14):            #weather data
        try:
            #print(line)
            date= line[0]    #weather data
            value = line[1]
            tag = line[2]
            #print value
            #skip processing the header line
            value = value.split(",")
            hr = value[0].split(":")[0]      #take out hour
            key = date+"^"+hr       #key assignment
            final_value = value[0]
            for i in range(1,len(line)):
                final_value += ','+line[i]
            print "%s\t%s\tW" %(key,final_value)
        except ValueError:
            pass
