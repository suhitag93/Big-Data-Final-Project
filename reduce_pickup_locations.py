#!/usr/bin/python

import sys

flag =False
passenger_sum = 0
prev_key = None
trip_count = 0

for line in sys.stdin:
    try:
        line = line.strip()
        key,passengers = line.split("\t")


        if flag==False:     #initialization
            prev_key = key
            passenger_sum = passengers
            trip_count =1
            flag=True
            continue

        if prev_key == key:      #for the same location
            passenger_sum += int(passengers)
            trip_count +=1

        else:                   #for a new location key

            print "%s,%s,%s" %(prev_key,passenger_sum,trip_count)
            passenger_sum = passengers
            trip_count = 1
            prev_key = key
        #key = pickup location coordinates
    except:
        pass
print "%s,%s,%s" %(prev_key,passenger_sum,trip_count)
